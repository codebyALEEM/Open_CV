# MULTIPLE COLOR DETECTION USING OPENCV

import cv2
import numpy as np

# Capture video from webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()
    
    # Convert the frame from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ------------------- RED COLOR DETECTION -------------------
    # Define HSV range for red color
    # (You can find these values experimentally using a color picker or testing)
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    
    # Create a mask for red color
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    
    # Extract red regions from the original frame
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # ------------------- BLUE COLOR DETECTION -------------------
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # ------------------- GREEN COLOR DETECTION -------------------
    low_green = np.array([40, 100, 100])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # ------------------- EVERY COLOR EXCEPT WHITE -------------------
    low = np.array([0, 42, 0])  # Minimum saturation > 42 excludes white
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # ------------------- DISPLAY -------------------
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Red Color Detection", red)
    cv2.imshow("Blue Color Detection", blue)
    cv2.imshow("Green Color Detection", green)
    cv2.imshow("All Colors Except White", result)

    # Press 'ESC' key to exit
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
