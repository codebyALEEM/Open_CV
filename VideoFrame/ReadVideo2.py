# video is nothing 1 image after another image
# if i press key then it keep goes to the next frame.

import cv2

import numpy as np

cap = cv2.VideoCapture(r"C:\Users\VICTUS\Desktop\mastering git\Practise git\Open_CV\VideoFrame\los_angeles.mp4")

while True:
    _, frame = cap.read()
    cv2.imshow("Frame", frame)
    cv2.waitKey(0)
