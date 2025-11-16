# OBJECT DETECTION USING OPENCV 

# We have 3 colors to detect: 1> Red  2> Green  3> Blue
# The goal is to detect a specific color in real-time using OpenCV.

import cv2
import numpy as np

# Capture video from the webcam (0 is the default camera; change to 1, 2, etc. for other cameras)
cap = cv2.VideoCapture(0)

# Start an infinite loop to read frames from the webcam
while True:
    _, frame = cap.read()  # Read a frame from the camera
    
    # Convert the frame from BGR (Blue, Green, Red) to HSV (Hue, Saturation, Value)
    # HSV makes it easier to detect and isolate specific colors
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Display the original frame in a window
    cv2.imshow("Frame", frame) 
    
    # Wait for a key press
    # If 'ESC' (key 27) is pressed, break the loop and stop the webcam
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
