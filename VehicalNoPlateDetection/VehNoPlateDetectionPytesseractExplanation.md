
---

# **License Plate Detection Using OpenCV and Pytesseract (Local System Version)**

This document explains — **step by step** and **line by line** — how a beginner can detect a license plate from an image locally and extract its text using **OpenCV** and  **Pytesseract** .

Every cell of your script is explained exactly in the order you wrote it.

---

# **📌 Introduction**

In this project, we detect a license plate from a vehicle image using:

* **OpenCV** → Image processing & contour detection
* **Imutils** → Helpful utility functions (mainly resizing)
* **Pytesseract** → OCR engine to read text from license plates

This method works  **offline** , directly on your  **local system** .

---

# **📦 Required Libraries**

```python
import cv2
import imutils  # We will need this library to resize our images.
import pytesseract  # We will need this library to extract the license plate text from the detected license plate.
```

### **Explanation**

* **cv2** → Main OpenCV library
* **imutils** → Simplifies resizing and other OpenCV operations
* **pytesseract** → Python wrapper for Google Tesseract OCR engine

---

# **🔧 Step 1 — Configure Tesseract Path**

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\AVSCODE\7. OPENCV\ocr'
```

### **Explanation**

* Points Python to the **location of the Tesseract executable** installed on your system.
* Without this, `pytesseract`  **cannot extract text** .

⚠️ **Important:**

You MUST have Tesseract installed locally.

Pytesseract cannot work without it.

---

# **🖼️ Step 2 — Load and Display Image**

```python
image = cv2.imread(r'C:\Users\Admin\AVSCODE\7. OPENCV\ocr\images.jpg')
resized_image = imutils.resize(image)
cv2.imshow('original image', image)
cv2.waitKey(0)
```

### **Explanation**

* Loads the vehicle image from your system.
* Resizes it for easier processing.
* Displays the original image.

---

# **⚪ Step 3 — Convert to Grayscale**

```python
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("greyed image", gray_image)
cv2.waitKey(0)
```

### **Explanation**

* Converts the image into grayscale.
* Makes edge detection easier and reduces noise.

---

# **✨ Step 4 — Smoothen the Image**

```python
gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
cv2.imshow("smoothened image", gray_image)
cv2.waitKey(0)
```

### **Explanation**

* Bilateral Filter → removes noise while keeping edges sharp.
* Ideal for detecting number plate outlines.

---

# **⚡ Step 5 — Edge Detection**

```python
edged = cv2.Canny(gray_image, 30, 200)
cv2.imshow("edged image", edged)
cv2.waitKey(0)
```

### **Explanation**

* Uses the **Canny** method to detect strong edges.
* License plate edges will stand out here.

---

# **🔍 Step 6 — Find All Contours**

```python
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
image1 = image.copy()
cv2.drawContours(image1, cnts, -1, (0, 255, 0), 3)
cv2.imshow("contours", image1)
cv2.waitKey(0)
```

### **Explanation**

* Retrieves **all contours** (shapes) in the image.
* Draws them on a copy of the image so you can visualize everything to start with.

---

# **✂️ Step 7 — Select the Top 30 Biggest Contours**

```python
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
screenCnt = None
image2 = image.copy()
cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)
cv2.imshow("Top 30 contours", image2)
cv2.waitKey(0)
```

### **Explanation**

* License plates are usually among the  **largest contours** .
* Keeps top **30** contours.
* Shows only those for better clarity.

---

# **🟩 Step 8 — Detect Rectangle & Crop Plate**

```python
i = 7
for c in cnts:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
    if len(approx) == 4:
        screenCnt = approx
        x, y, w, h = cv2.boundingRect(c)
        new_img = image[y:y+h, x:x+w]
        cv2.imwrite('./'+str(i)+'.png', new_img)
        i += 1
        break
```

### **Explanation**

* Loops through contours.
* Approximates them into polygons.
* Checks for **4-sided shapes** → possible license plate.
* Crops that region.
* Saves it (7.png, 8.png, etc.).

---

# **🖼️ Step 9 — Draw Final Detected Plate**

```python
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("image with detected license plate", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### **Explanation**

* Highlights the final detected license plate in green.
* Displays it.
* Closes all windows.

---

# **🔤 Step 10 — Extract Text Using Pytesseract**

```python
plate_text = pytesseract.image_to_string(new_img)
print("Detected License Plate Text:", plate_text)
```

### **Explanation**

* Sends the cropped plate image to Tesseract OCR.
* Recognizes and prints the license plate number.

---

# **📘 About Pytesseract (Important Section)**

Pytesseract is a Python wrapper for the  **Tesseract OCR Engine** , originally developed by HP and later improved by Google.

### ✔ Features

* Reads printed text from images.
* Supports multiple languages.
* Works with OpenCV, PIL, and NumPy images.
* Can extract:
  * License plate numbers
  * Document text
  * Signboards
  * Numbers & handwritten-like printed text

### ⚠ Limitations

* Requires **Tesseract to be installed locally** → extremely important.
* Not as accurate on noisy or very small text.
* Not GPU-accelerated like EasyOCR or PaddleOCR.

---

# **🌐 Reference to Your Streamlit-based Project**

You also have another implementation:

### 🔗 **File:** StreamlitVehicalNumberPlateDetection.py

This file performs  **license plate detection only** , using OpenCV and Streamlit for a  **web-based UI** ,  *without text extraction* .

### ✔ Differences Between Both Files

| Local Script (This MD)         | Streamlit Script                     |
| ------------------------------ | ------------------------------------ |
| Performs OCR using Pytesseract | No OCR, only detection               |
| Requires Tesseract installed   | Works fully online without Tesseract |
| Runs locally                   | Runs via web UI                      |
| Saves cropped images           | Displays cropped region in app       |

Both files can be included in the same repo —

**local version (with OCR)** and  **web version (frontend only)** .

---

# **✅ Summary**

This project performs:

1. Load image
2. Convert to grayscale
3. Smooth and reduce noise
4. Detect edges
5. Find contours
6. Select top candidates
7. Detect 4-point license plate region
8. Crop the license plate
9. Highlight it
10. Extract text using Pytesseract

Everything is beginner-friendly and explained line-by-line.

---

# **🎯 End of Document**
