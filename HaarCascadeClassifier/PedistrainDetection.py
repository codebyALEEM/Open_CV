import cv2
import numpy as np
import os

# Set the path for the body classifier (Haar Cascade XML)
body_classifier_path = r'C:\Users\VICTUS\Desktop\NIT\A1-July\58~ 13th- Haar cascade classifier\13th- Haar cascade classifier\Haarcascades\haarcascade_fullbody.xml'

# Check if the classifier path exists
if not os.path.exists(body_classifier_path):
    print(f"Error: The calssifier file does not exist at {body_classifier_path}")
    exit()
  
# Open the video file
cap = cv2.VideoCapture(r"C:\Users\VICTUS\Desktop\open_cv\PedestrainVideo.mov")
    
# Create the body classifier using the provided path   
body_classifier = cv2.CascadeClassifier(body_classifier_path)

# Check if the classifier is loaded successfully
if body_classifier.empty():
    print("Error: Could not lead the body classifier.Make sure the XML file valid  and accessible.")
    exit()
    
print("Video open Succcessfully.Starting pedestrian detection...")

while cap.isOpened():
    ret, frame = cap.read()
    

    # If frame is not read correctly, exit the loop
    if not ret:
        print("Error: Failed to read frame from video. Exiting...")
        break

    # Convert the frame to grayscale for better detection performance
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect bodies in the grayscale image
    bodies = body_classifier.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(120, 120), flags=cv2.CASCADE_SCALE_IMAGE)

    # Draw bounding boxes for detected bodies
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

    # Display the result with detected bodies
    cv2.imshow('Pedestrians', frame)

    # Press Enter (13) to exit
    if cv2.waitKey(1) == 13:  # 13 corresponds to the Enter key
        print("Exiting...")
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()   
 