# Color Detection Using OpenCV

This project demonstrates how to detect different colors in real-time using a webcam with OpenCV. It covers detecting **Red, Green, Blue**, and **all colors except white**.

---

## **Introduction**

Color detection is a process of identifying specific colors in an image or video. This can be used in many applications, such as:

- Sorting objects by color
- Traffic light detection
- Games or interactive applications
- Robotics

OpenCV (Open Source Computer Vision Library) is a popular library in Python for image and video processing.  

In this project, we use **HSV color space**, which makes it easier to detect colors compared to the default **BGR color space**.

---

## **Understanding Color Spaces**

### **BGR**
- OpenCV uses BGR (Blue, Green, Red) by default.
- Each pixel has three values representing the intensity of blue, green, and red.

### **HSV**
- Stands for **Hue, Saturation, Value**.
- Hue = type of color (0-179 in OpenCV)
- Saturation = intensity/purity of color
- Value = brightness
- HSV separates color information from brightness, making it easier to detect a specific color regardless of lighting.

---

## **Required Libraries**

```python
import cv2
import numpy as np
```

- `cv2` is OpenCV, used for image and video processing.
- `numpy` is used to create arrays for color ranges (HSV limits).

---

## **Step 1: Capturing Webcam Video**

```python
cap = cv2.VideoCapture(0)
```

- `0` means the default webcam.
- If you have multiple cameras, you can use `1`, `2`, etc.
- `cap.read()` reads frames from the camera one by one.

---

## **Step 2: Converting BGR to HSV**

```python
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

- Converts the captured frame to HSV format.
- Easier to detect colors in HSV than in BGR.

---

## **Step 3: Detecting Colors**

We define **lower and upper bounds** for each color in HSV. Then we create a **mask** that isolates that color.

### **Red Color Detection**

```python
low_red = np.array([161, 155, 84])
high_red = np.array([179, 255, 255])
red_mask = cv2.inRange(hsv_frame, low_red, high_red)
red = cv2.bitwise_and(frame, frame, mask=red_mask)
```

- `np.array([low_H, low_S, low_V])` = lower bound of color in HSV.
- `np.array([high_H, high_S, high_V])` = upper bound of color in HSV.
- `cv2.inRange()` creates a **mask** where the pixels within the color range are white, others are black.
- `cv2.bitwise_and()` keeps only the parts of the frame where the mask is white.

### **Blue Color Detection**

```python
low_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])
blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
```

### **Green Color Detection**

```python
low_green = np.array([40, 100, 100])
high_green = np.array([102, 255, 255])
green_mask = cv2.inRange(hsv_frame, low_green, high_green)
green = cv2.bitwise_and(frame, frame, mask=green_mask)
```

### **All Colors Except White**

```python
low = np.array([0, 42, 0])
high = np.array([179, 255, 255])
mask = cv2.inRange(hsv_frame, low, high)
result = cv2.bitwise_and(frame, frame, mask=mask)
```

- White has very low saturation in HSV, so setting **minimum saturation > 40** excludes white.
- All other colors remain.

---

## **Step 4: Displaying Results**

```python
cv2.imshow("Original Frame", frame)
cv2.imshow("Red Color Detection", red)
cv2.imshow("Blue Color Detection", blue)
cv2.imshow("Green Color Detection", green)
cv2.imshow("All Colors Except White", result)
```

- Each color detection is displayed in a separate window.
- `cv2.waitKey(1)` waits for 1 millisecond for a key press.
- Press **ESC (27)** to exit the program.

---

## **Step 5: Release Resources**

```python
cap.release()
cv2.destroyAllWindows()
```

- Always release the webcam when done.
- Close all OpenCV windows to free up memory.

---

## **How to Find HSV Values**

- You can use a **color picker tool** or test manually.
- HSV values vary depending on lighting and camera quality.
- Example: Red `[161, 155, 84]` to `[179, 255, 255]` was determined experimentally.

---

## **Summary**

- OpenCV allows real-time detection of specific colors using **HSV masks**.
- `cv2.inRange()` and `cv2.bitwise_and()` are the main tools to isolate colors.
- This project can be extended to label objects, track movements, or detect multiple colors in the same frame.

---

*End of Document*

