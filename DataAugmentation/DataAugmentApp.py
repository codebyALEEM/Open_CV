import streamlit as st
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array
from PIL import Image
import numpy as np

st.title("📸 Image Augmentation Viewer")

# Init session state to avoid re-running the generator
if "generated_images" not in st.session_state:
    st.session_state.generated_images = None

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
num_images = st.slider("Number of augmented images", 1, 50, 10)

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Original Image")

    img = img.resize((150, 150))
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    if st.button("Generate Augmented Images"):
        generated = []
        count = 0

        # Create a NEW generator every time
        flow = datagen.flow(x, batch_size=1)

        while count < num_images:
            batch = next(flow)
            arr = batch[0].astype("uint8")
            generated.append(Image.fromarray(arr))
            count += 1

        # Save result in session state to prevent re-generating
        st.session_state.generated_images = generated

# Display ONLY what is stored (prevents 1→2→3 issue)
if st.session_state.generated_images:
    st.success(f"Showing {len(st.session_state.generated_images)} images")
    
    cols = st.columns(5)
    for i, aug in enumerate(st.session_state.generated_images):
        cols[i % 5].image(aug, width=250)
