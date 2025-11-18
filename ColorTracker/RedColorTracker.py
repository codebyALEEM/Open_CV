# DETECT RED COLOR USING OPENCV

import cv2
import numpy as np

# Capture video from webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()
    
    # Convert the frame from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the range for red color in HSV
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    
    # Create a mask to isolate red color
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    
    # Apply the mask on the original frame to extract red regions
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    
    # Display the original frame and the red-detected frame
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Red Color Detection", red)
    
    # Press 'ESC' key to exit
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
