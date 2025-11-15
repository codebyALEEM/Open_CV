import streamlit as st
import cv2
import tempfile
import numpy as np

st.set_page_config(page_title="Car Detection App", layout="wide")
st.title("🚗 Car Detection using Haar Cascade")

# -----------------------------
# FIXED XML PATH (YOUR PATH)
# -----------------------------
car_classifier_path = r'C:\Users\VICTUS\Desktop\NIT\A1-July\58~ 13th- Haar cascade classifier\13th- Haar cascade classifier\Haarcascades\haarcascade_car.xml'

# Load classifier
car_classifier = cv2.CascadeClassifier(car_classifier_path)

if car_classifier.empty():
    st.error("❌ Could not load Haar Cascade. Check the XML path!")
else:
    st.success("✅ Haar Cascade loaded successfully!")

# -----------------------------
# Video Upload
# -----------------------------
video_file = st.file_uploader("Upload Car Video", type=["mp4", "avi", "mov"])

if video_file is not None:

    # Save uploaded video temporarily
    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_video.write(video_file.read())
    temp_video.close()

    st.info("▶️ Processing video...")

    cap = cv2.VideoCapture(temp_video.name)

    frame_display = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            st.warning("Video has ended or cannot read frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cars = car_classifier.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30)
        )

        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

        # Streamlit display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_display.image(frame_rgb, channels="RGB")

    cap.release()

else:
    st.warning("👆 Please upload a video to start detection.")
