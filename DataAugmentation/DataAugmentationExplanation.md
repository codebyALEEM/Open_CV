# Image Augmentation Frontend -- Full Explanation (Markdown)

This file explains every line of the Streamlit-based image augmentation
frontend to understand what is happening.

------------------------------------------------------------------------

## 🧠 Introduction

This application allows you to upload an image and generate many new
versions of it by applying random transformations (rotation, zoom, flip,
etc.).\
This technique is called **Image Augmentation**, and it helps machine
learning models train better.

------------------------------------------------------------------------

## 📌 Code Explanation (Line-by-Line)

### **Importing required libraries**

``` python
import streamlit as st
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array
from PIL import Image
import numpy as np
```

-   `streamlit` → used to create the web interface.\
-   `ImageDataGenerator` → creates modified versions of the image.\
-   `img_to_array` → converts images into numeric format.\
-   `PIL.Image` → loads and displays images.\
-   `numpy` → handles mathematical operations.

------------------------------------------------------------------------

### **Title of the webpage**

``` python
st.title("📸 Image Augmentation Viewer")
```

This shows the title at the top of the app.

------------------------------------------------------------------------

### **Store generated images safely**

``` python
if "generated_images" not in st.session_state:
    st.session_state.generated_images = None
```

Streamlit refreshes the page on every action.\
`session_state` prevents losing generated images after the button click.

------------------------------------------------------------------------

### **Image upload option**

``` python
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
```

Creates a button for uploading images from your computer.

------------------------------------------------------------------------

### **Slider to choose how many images to generate**

``` python
num_images = st.slider("Number of augmented images", 1, 50, 10)
```

Lets you pick between 1 and 50 augmented images.

------------------------------------------------------------------------

### **Augmentation settings**

``` python
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)
```

These are the random transformations applied to create new images: -
Rotate by up to 40 degrees\
- Move image left-right\
- Move up-down\
- Shear (slant the image)\
- Zoom randomly\
- Flip horizontally\
- Fill any empty space intelligently

------------------------------------------------------------------------

### **Show uploaded image**

``` python
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Original Image", width=220)
```

If the user uploads an image:\
- Load the image\
- Display it on screen

------------------------------------------------------------------------

### **Resize and convert the image to numeric array**

``` python
img = img.resize((150, 150))
x = img_to_array(img)
x = x.reshape((1,) + x.shape)
```

-   Resizes the image to 150×150 pixels\
-   Converts the image into numbers\
-   Adds an extra dimension required by TensorFlow

------------------------------------------------------------------------

### **Button to generate images**

``` python
if st.button("Generate Augmented Images"):
```

Runs augmentation only when the user clicks the button.

------------------------------------------------------------------------

### **Prepare the generator**

``` python
generated = []
count = 0
flow = datagen.flow(x, batch_size=1)
```

-   `generated` stores output images\
-   `count` tracks how many images were created\
-   `flow` creates augmented images one-by-one

------------------------------------------------------------------------

### **Generate exactly the number asked**

``` python
while count < num_images:
    batch = next(flow)
    arr = batch[0].astype("uint8")
    generated.append(Image.fromarray(arr))
    count += 1
```

-   Gets images from the generator\
-   Converts numeric arrays back into images\
-   Stores them\
-   Stops exactly at `num_images`

------------------------------------------------------------------------

### **Save outputs in session so Streamlit doesn't regenerate**

``` python
st.session_state.generated_images = generated
```

Prevents the problem where it keeps generating more images on every
refresh.

------------------------------------------------------------------------

### **Show images on the screen**

``` python
if st.session_state.generated_images:
    st.success(f"Showing {len(st.session_state.generated_images)} images")

    cols = st.columns(5)
    for i, aug in enumerate(st.session_state.generated_images):
        cols[i % 5].image(aug, width=150)
```

-   Shows a success message\
-   Displays all generated images in a grid (5 images per row)

------------------------------------------------------------------------

## 🎯 Summary 

-   You upload a picture\
-   The system creates many new versions of that picture\
-   This helps AI models understand images better\
-   The webpage shows you all the generated images\
-   Nothing is saved unless you explicitly add saving functionality

------------------------------------------------------------------------

## ✅ End of Explanation
