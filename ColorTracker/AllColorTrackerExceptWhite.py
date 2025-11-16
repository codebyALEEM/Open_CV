# DETECT EVERY COLOR EXCEPT WHITE USING OPENCV

import cv2
import numpy as np

# Capture video from webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()
    
    # Convert the frame from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define HSV range for all colors except white
    # White has very low saturation, so by setting min saturation > 40, we exclude white
    low = np.array([0, 42, 0]) 
    high = np.array([179, 255, 255])
    
    # Create a mask to isolate all colors except white
    mask = cv2.inRange(hsv_frame, low, high)
    
    # Apply the mask on the original frame to extract colored regions
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame and the resulting frame
    cv2.imshow("Original Frame", frame) 
    cv2.imshow("Colors Except White", result)
    
    # Press 'ESC' key to exit
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
