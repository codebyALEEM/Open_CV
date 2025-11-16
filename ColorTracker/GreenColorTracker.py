# DETECT GREEN COLOR USING OPENCV

import cv2
import numpy as np

# Capture video from the webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()
    
    # Convert the frame from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define HSV range for green color
    low_green = np.array([40, 100, 100])
    high_green = np.array([102, 255, 255])
    
    # Create a mask to isolate green color
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    
    # Apply the mask on the original frame to extract green regions
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Display the original frame and the green-detected frame
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Green Color Detection", green)
    
    # Press 'ESC' key to exit
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
