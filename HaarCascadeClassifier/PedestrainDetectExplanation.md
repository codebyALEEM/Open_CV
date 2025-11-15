# Pedestrian Detection using Haar Cascade (OpenCV)

This project demonstrates how to detect pedestrians in a video using a **Haar Cascade Full-Body Classifier**, a classical computer vision technique from OpenCV.

It is an excellent educational example for understanding traditional object detection methods before transitioning into deep-learning-based approaches.

---

## 🧠 How It Works

1. Load the Haar Cascade XML model.
2. Load a video file.
3. Read each frame from the video.
4. Convert the frame to grayscale.
5. Detect pedestrians using the cascade classifier.
6. Draw bounding boxes around detected pedestrians.
7. Display the video output.
8. Repeat until the video ends or the user exits.

---

## ⚠️ Performance Note

Haar Cascade full-body detection is:

- **Lightweight** and easy to understand.
- **Useful for classical computer vision learning**.
- Naturally **slower and less accurate** on real-world pedestrian videos compared to newer deep-learning models.

This is expected, as Haar Cascades are one of the earliest object detection methods.

---

## 📄 Full Code (With Line-by-Line Explanation)

```python
import cv2
import numpy as np
import os
```

### ✔ Import necessary libraries

- `cv2`: OpenCV for image and video processing.
- `numpy`: numerical library (not heavily used here).
- `os`: used to verify file paths.

---

```python
body_classifier_path = r'C:\..\haarcascade_fullbody.xml'
```

### ✔ Path to the Haar Cascade file

This XML file contains the pretrained model for full-body pedestrian detection.

---

```python
if not os.path.exists(body_classifier_path):
    print(f"Error: The calssifier file does not exist at {body_classifier_path}")
    exit()
```

### ✔ Check if the classifier file exists

Prevents runtime errors by confirming the XML file is present.

---

```python
cap = cv2.VideoCapture(r"C:\...\Pedestrain1.mov")
```

### ✔ Open the input video file

Reads frames one by one.

---

```python
body_classifier = cv2.CascadeClassifier(body_classifier_path)
```

### ✔ Load the Haar Cascade classifier

This initializes the pedestrian detector.

---

```python
if body_classifier.empty():
    print("Error: Could not lead the body classifier.Make sure the XML file valid  and accessible.")
    exit()
```

### ✔ Validate classifier loading

If OpenCV fails to read the XML, program exits gracefully.

---

```python
print("Video open Succcessfully.Starting pedestrian detection...")
```

### ✔ Status message

Indicates detection is about to begin.

---

```python
while cap.isOpened():
```

### ✔ Loop through each frame of the video

Runs until the video ends.

---

```python
    ret, frame = cap.read()
```

### ✔ Read the next frame

- `ret` = success flag.
- `frame` = image.

---

```python
    if not ret:
        print("Error: Failed to read frame from video. Exiting...")
        break
```

### ✔ Stop if video ends or frame read fails

Protects against infinite loop errors.

---

```python
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

### ✔ Convert frame to grayscale

Haar Cascades require grayscale images for detection.

---

```python
    bodies = body_classifier.detectMultiScale(
        gray, scaleFactor=1.05, minNeighbors=5, minSize=(120, 120),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
```

### ✔ Detect pedestrians

Parameter breakdown:

- **gray**: input grayscale frame.
- **scaleFactor=1.05**: how much image size reduces per detection scale.
- **minNeighbors=5**: higher = more reliable detections.
- **minSize=(120,120)**: minimum detection window.
- **flags**: standard OpenCV settings.

This returns a list of bounding boxes.

---

```python
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
```

### ✔ Draw rectangles around detected pedestrians

Yellow bounding boxes highlight detected individuals.

---

```python
    cv2.imshow('Pedestrians', frame)
```

### ✔ Display the frame

Shows the processed video with detections.

---

```python
    if cv2.waitKey(1) == 13:
        print("Exiting...")
        break
```

### ✔ Exit when the user presses ENTER (key code 13)

Allows manual termination.

---

```python
cap.release()
cv2.destroyAllWindows()
```

### ✔ Cleanup operations

- Releases the video.
- Closes all OpenCV windows.

---

## 🚀 Summary

This project shows how classical Haar Cascade–based pedestrian detection works. Though it may be slower and less accurate compared to modern deep learning models, it remains an important foundational technique in computer vision.

---

##

