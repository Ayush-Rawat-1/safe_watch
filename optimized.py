import cv2
import torch
import pandas as pd
import numpy as np
from ultralytics import YOLO
from gender_detection import detectGender

model = YOLO("yolov8n-pose.pt")

cap = cv2.VideoCapture("./sample_video.mp4")

if not cap.isOpened():
    print("Error: Could not open video.")

# Initialize dictionaries to store detected regions
dict_data = {'x1':[], 'y1':[], 'x2':[], 'y2':[]}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    results = model(frame)
    var = results[0].boxes.data
    
    # Move the tensor to CPU and convert to NumPy array
    var = var.cpu().numpy()
    
    # Adjust columns based on actual data structure
    if var.shape[1] == 6:
        columns = ['x1', 'y1', 'x2', 'y2', 'confidence', 'class']
    elif var.shape[1] == 4:
        columns = ['x1', 'y1', 'x2', 'y2']
    else:
        print("Unexpected shape of var. Columns cannot be determined.")
        continue
    
    try:
        px = pd.DataFrame(var, columns=columns)
    except ValueError as e:
        print("Error creating DataFrame:", e)
        continue
    
    # Create DataFrames for male and female regions
    MG = pd.DataFrame(dict_data)
    FG = pd.DataFrame(dict_data)
    
    # Process each detected bounding box
    for index, row in px.iterrows():
        x1 = int(row['x1'])
        y1 = int(row['y1'])
        x2 = int(row['x2'])
        y2 = int(row['y2'])
        
        # Crop the frame and detect gender
        cropped_frame = frame[y1:y2, x1:x2]
        gender = detectGender(cropped_frame)
        
        if gender == 1:
            FG.loc[len(FG)] = [x1, y1, x2, y2]
        else:
            MG.loc[len(MG)] = [x1, y1, x2, y2]
    
    # Check for overlapping regions
    for i in FG.index:
        x1 = FG['x1'][i]
        y1 = FG['y1'][i]
        x2 = FG['x2'][i]
        y2 = FG['y2'][i]
        
        for id in MG.index:
            x11 = MG['x1'][id]
            y11 = MG['y1'][id]
            x22 = MG['x2'][id]
            y22 = MG['y2'][id]
            
            if (y11 >= y1 and y11 <= y2) or (y22 >= y1 and y22 <= y2):
                if (x11 >= x1 and x11 <= x2) or (x22 >= x1 and x22 <= x2):
                    print("Threat")
    
    # Display the frame
    cv2.imshow("Pose Detection", frame)
    
    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()