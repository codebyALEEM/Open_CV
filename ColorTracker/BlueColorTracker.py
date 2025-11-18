# DETECT BLUE COLOR USING OPENCV

import cv2
import numpy as np

# Capture video from the webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:    
    # Read each frame from the webcam
    _, frame = cap.read()
    
    # Convert the frame from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define HSV range for blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    
    # Create a mask to isolate blue color
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    
    # Apply the mask on the original frame to extract blue regions
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # Display the original frame and the blue-detected frame
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Blue Color Detection", blue)
    
    # Press 'ESC' key to exit
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
