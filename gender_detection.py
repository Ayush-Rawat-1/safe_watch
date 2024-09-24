import cv2
import pandas as pd
import supervision as sv
from ultralytics import YOLOWorld

# model = YOLOWorld("yolov8s-worldv2.pt") #on cpu
model =YOLOWorld("yolov8l-worldv2.pt").to("cuda")
# classes=["men","women"]
classes = ["men", "man", "male", "female", "women","woman"]
model.set_classes(classes)

def detectGender(image):
    results = model.predict(image,conf=0.1)
    
    detections = sv.Detections.from_ultralytics(results[0]).with_nms(threshold=0.5)
    labels = [
        (class_id,confidence)
        for class_id, confidence
        in zip(detections.class_id, detections.confidence)
    ]
    max_label = max(labels, key=lambda x: x[1])
    class_id_with_max_confidence = max_label[0]
    if(class_id_with_max_confidence > 2):
        return 1
    else:
        return 0