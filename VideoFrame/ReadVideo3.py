
# it will display the complete video

import cv2

import numpy as np

cap = cv2.VideoCapture(r"C:\Users\VICTUS\Desktop\mastering git\Practise git\Open_CV\VideoFrame\los_angeles.mp4")

while True:
    _, frame = cap.read()
    
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()