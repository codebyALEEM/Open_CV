# Detect the objects  


import cv2

import numpy as np

cap = cv2.VideoCapture(r"C:\Users\VICTUS\Desktop\mastering git\Practise git\Open_CV\VideoFrame\los_angeles.mp4")

_, frame = cap.read()

cv2.imshow("Frame", frame)
cv2.waitKey(0)


    

