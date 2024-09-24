Project Title:  SafeWatch : Threat Detection System for Women's Safety

Problem Statement:
As crime rates against women continue to rise in urban environments, there is an urgent need for smarter surveillance and analytics systems. Traditional security systems often fail to detect potential dangers in real-time, which delays the response of law enforcement and limits the ability to prevent incidents before they escalate. A more proactive, automated solution is essential to ensure the safety of women in public areas by identifying risks early on and enabling timely intervention.

Objective:
This project aims to develop a Women’s Safety Analytics platform that enhances protection through continuous real-time monitoring. The system will identify and assess potential risks based on the behavior and interactions of individuals in monitored zones, while also recognizing critical emergency gestures to trigger immediate responses.

Proposed Solution:
The system utilizes the YOLO object detection model for accurate detection of individuals and gender classification. By extracting bounding box coordinates, it categorizes people into males and females and keeps count of each group within a given area. If only one female is detected, she is flagged as a “lone woman,” triggering an increase in the threat level. Additionally, the system applies an overlapping analysis to assess the proximity between detected females and nearby males, using their positional coordinates. If the overlap exceeds a predetermined threshold and continues over an extended period, the threat level is further elevated. To enhance safety, MediaPipe is integrated to recognize emergency gestures in real-time, such as raising both hands, which triggers an instant alert for help.

Expected Outcome:
This system will drastically improve the real-time identification of potential dangers, allowing for quicker interventions to safeguard women in vulnerable situations. It will also provide valuable data on risk-prone areas, assisting law enforcement in long-term safety planning and crime prevention strategies.
