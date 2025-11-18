import streamlit as st
import cv2
import imutils
import numpy as np
from PIL import Image
import io


def simple_plate_detect(image_np):
    """
    Detect and crop the license plate using OpenCV contour detection.
    Returns:
      - Cropped plate image (if found)
      - Image with contour drawn
    """

    # Resize for consistent processing
    image = imutils.resize(image_np, width=600)

    # ---- Preprocessing ----
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    # ---- Edge Detection ----
    edged = cv2.Canny(gray, 30, 200)

    # ---- Find Contours ----
    cnts, _ = cv2.findContours(
        edged.copy(),
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Sort by largest contours (top 10)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]

    screenCnt = None
    cropped_plate = None

    # ---- Look for 4-Sided Shape (Plate Shape) ----
    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)

        if len(approx) == 4:     # rectangle / quadrilateral
            screenCnt = approx
            x, y, w, h = cv2.boundingRect(c)
            cropped_plate = image[y:y+h, x:x+w]
            break

    # ---- Draw Contour and Return ----
    display_image = image.copy()

    if screenCnt is not None:
        cv2.drawContours(display_image, [screenCnt], -1, (0, 255, 0), 3)
        return cropped_plate, display_image
    else:
        return None, display_image



st.title("🚗 License Plate Detector ")
st.markdown("Upload a vehicle image to **detect & crop** the license plate.")

# ---- File Upload ----
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Convert file to OpenCV image (BGR)
        image_bytes = uploaded_file.read()
        file_bytes = np.asarray(bytearray(image_bytes), dtype=np.uint8)
        image_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        st.subheader("🖼️ Original Image Analysis")

        # Run Plate Detection
        cropped_plate, image_with_contour = simple_plate_detect(image_bgr)

        # Convert image for display (BGR → RGB)
        image_display = cv2.cvtColor(image_with_contour, cv2.COLOR_BGR2RGB)
        st.image(image_display, caption="Detected Plate Contour", use_column_width=True)

        # ---- Display Cropped Plate ----
        if cropped_plate is not None:
            st.success("✅ License Plate Detected!")

            cropped_rgb = cv2.cvtColor(cropped_plate, cv2.COLOR_BGR2RGB)
            st.subheader("✂️ Cropped Number Plate")
            st.image(cropped_rgb, caption="Ready for OCR", width=300)

            st.markdown("---")
            st.info("💡 **Next Step:** Integrate EasyOCR or PaddleOCR to extract text.")

        else:
            st.error("❌ License plate not detected. Try a clearer image.")

    except Exception as e:
        st.error(f"⚠️ Error during processing: {e}")
        
        
        

#     ADD BACKGROUND IMAGE
st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://static.vecteezy.com/system/resources/previews/023/915/211/non_2x/foreign-matter-detection-radar-technology-control-screen-background-it-is-a-screen-suitable-for-using-modern-technology-using-it-as-a-poster-or-background-emphasize-the-use-of-dark-blue-tones-vector.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
    </style>
    """,
    unsafe_allow_html=True
)
