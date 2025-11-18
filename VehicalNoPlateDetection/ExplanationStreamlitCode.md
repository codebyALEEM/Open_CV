
---

# 🚗 License Plate Detection Web App (Streamlit + OpenCV)

This document explains how a complete license plate detection system works using **OpenCV** for image processing and **Streamlit** for creating an interactive web interface.

This explanation follows a  **beginner-friendly style** , covering every step and every line so anyone can understand the entire code flow.

---

## **Introduction**

License plate detection involves identifying the rectangular region containing a vehicle’s number plate and cropping it out for later OCR (Optical Character Recognition).

This application:

* Accepts an image uploaded by the user,
* Processes it using OpenCV,
* Detects the license plate area using contours,
* Draws its boundary,
* Crops the plate region,
* Displays both the processed image and cropped plate.

We use:

* **OpenCV (cv2)** → Image processing & contour detection
* **imutils** → Easy image resizing
* **NumPy** → Array operations
* **Streamlit** → Frontend UI
* **PIL** → Image format handling

---

# ----------------------------------------------

# **1. Import Required Libraries**

# ----------------------------------------------

```python
import streamlit as st
import cv2
import imutils
import numpy as np
from PIL import Image
import io
```

### **Explanation**

* `streamlit` → Used to build the web user interface.
* `cv2` → Main library for computer vision tasks like grayscale conversion, edge detection, and contour analysis.
* `imutils` → Provides simpler functions to resize images.
* `numpy` → Converts uploaded files into arrays OpenCV can process.
* `PIL.Image` → Helps handle image formats if needed.
* `io` → Provides in-memory byte operations (not heavily used here but available).

---

# ===================================================================

# **2. License Plate Detection Function**

# ===================================================================

This function takes an image, processes it, finds a plate-shaped contour, and returns:

* Cropped license plate
* Image with contour drawn around the detected plate

---

## **Function Definition**

```python
def simple_plate_detect(image_np):
```

Defines a reusable detection function.

---

## **Step 1: Resize Image**

```python
image = imutils.resize(image_np, width=600)
```

* Ensures all images are processed at a standard size for consistent detection.

---

## **Step 2: Preprocessing**

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
```

Breakdown:

* Converts the image to **grayscale** → removes color complexity
* Applies **bilateral filtering** → removes noise but keeps edges sharp

  (important for better contour and edge detection)

---

## **Step 3: Edge Detection**

```python
edged = cv2.Canny(gray, 30, 200)
```

* Canny algorithm finds edges in the preprocessed image
* Helps highlight sharp boundaries like number plates

---

## **Step 4: Find Contours**

```python
cnts, _ = cv2.findContours(
    edged.copy(),
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_SIMPLE
)
```

* Finds all continuous boundaries (contours) in the edge image
* `RETR_LIST` → retrieves ALL contours
* `CHAIN_APPROX_SIMPLE` → compresses contour points for efficiency

---

## **Step 5: Select Top 10 Contours**

```python
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
```

* Sorts contours by area
* Keeps largest 10 since plates are usually among the bigger contours

---

## **Step 6: Look for a 4-sided Shape (Rectangle)**

```python
screenCnt = None
cropped_plate = None

for c in cnts:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)

    if len(approx) == 4:
        screenCnt = approx
        x, y, w, h = cv2.boundingRect(c)
        cropped_plate = image[y:y+h, x:x+w]
        break
```

Explanation:

* Approximates each contour into a polygon
* Checks if it has exactly **4 sides** → possible license plate
* Once found:
  * Stores its contour points
  * Extracts the bounding rectangle
  * Crops the area containing the plate

This ends the search after the first valid rectangle.

---

## **Step 7: Draw Contour & Return Results**

```python
display_image = image.copy()

if screenCnt is not None:
    cv2.drawContours(display_image, [screenCnt], -1, (0, 255, 0), 3)
    return cropped_plate, display_image
else:
    return None, display_image
```

* Draws a green contour on the detected plate
* Returns:
  * Cropped plate (if detected)
  * Image with contour

---

# ===================================================================

# **3. Streamlit Web App UI**

# ===================================================================

This part builds the **frontend UI** for uploading images and displaying results.

---

## **App Title & Description**

```python
st.title("🚗 License Plate Detector (OpenCV)")
st.markdown("Upload a vehicle image to detect & crop the license plate.")
```

* Creates the title
* Adds a short description using Markdown

---

## **File Upload Widget**

```python
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
```

* Allows users to upload images
* Restricts to JPG/PNG formats

---

## **If User Uploads an Image**

```python
if uploaded_file is not None:
    try:
```

We start processing only if a valid file is uploaded.

---

## **Convert Uploaded File to OpenCV Format**

```python
image_bytes = uploaded_file.read()
file_bytes = np.asarray(bytearray(image_bytes), dtype=np.uint8)
image_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
```

Step-by-step:

* Reads the raw image bytes
* Converts them into a NumPy byte array
* Decodes into an OpenCV-style image (BGR format)

---

## **Analyze & Display the Image**

```python
st.subheader("🖼️ Original Image Analysis")
```

---

## **Run License Plate Detection**

```python
cropped_plate, image_with_contour = simple_plate_detect(image_bgr)
```

* Calls our detection function
* Receives:
  * Cropped plate
  * Image with contour

---

## **Convert BGR → RGB for Streamlit display**

```python
image_display = cv2.cvtColor(image_with_contour, cv2.COLOR_BGR2RGB)
st.image(image_display, caption="Detected Plate Contour", use_column_width=True)
```

* Streamlit expects RGB images
* OpenCV stores images in BGR → conversion required

---

## **If Plate Found: Show Cropped Plate**

```python
if cropped_plate is not None:
    st.success("✅ License Plate Detected!")

    cropped_rgb = cv2.cvtColor(cropped_plate, cv2.COLOR_BGR2RGB)
    st.subheader("✂️ Cropped Number Plate")
    st.image(cropped_rgb, caption="Ready for OCR", width=300)

    st.markdown("---")
    st.info("💡 Next Step: Integrate EasyOCR or PaddleOCR to extract text.")
```

* Displays the cropped plate
* Gives a success message
* Recommends next step (OCR)

---

## **If Plate Not Found**

```python
else:
    st.error("❌ License plate not detected. Try a clearer image.")
```

* Shows an error

---

## **Error Handling**

```python
except Exception as e:
    st.error(f"⚠️ Error during processing: {e}")
```

Handles unexpected issues such as:

* Corrupted files
* Unsupported formats
* Decoding errors

---

# ===================================================================

# **Extra Features of the Libraries Used**

# ===================================================================

## **OpenCV (cv2)**

* Edge detection (Canny)
* Contour extraction
* Grayscale conversion
* Image resizing & cropping
* Real-time video processing capability

## **imutils**

* Simplifies resizing
* Works as a wrapper for OpenCV convenience
* Avoids writing long code like `cv2.resize()` repeatedly

## **Streamlit**

* Turns Python scripts into web apps instantly
* Drag-and-drop file upload
* Live components like images, buttons, alerts
* No HTML/CSS/JS required
* Auto-reload on code changes

## **NumPy**

* Converts raw files to image arrays
* Used internally by OpenCV for image operations

---

# ===================================================================

# **Summary**

# ===================================================================

This project performs:

1. **Image upload** via Streamlit
2. **Image preprocessing** (resize → grayscale → smoothing)
3. **Edge detection** using Canny
4. **Contour detection**
5. **Find a 4-sided shape** (probable plate)
6. **Crop the license plate**
7. **Display results online**
8. **Suggest OCR as next step**

This full workflow allows beginners to understand how computer vision + UI integration works in a real project.
