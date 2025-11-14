import cv2 
import numpy as np
import gradio as gr

face_classifier = cv2.CascadeClassifier(r'C:\Users\VICTUS\Downloads\haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier(r'C:\Users\VICTUS\Downloads\haarcascade_eye.xml')

def detect_face_and_eyes(image):
    
    img = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    
    if len(faces) == 0:
        text = "No Face Found"
    else:
        text = f"{len(faces)} Face(s) Detected"
        
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,255),2)
        
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y +h, x:x + w]
        
        eyes = eye_classifier.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey + eh),(255,255,0),2)
        
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    return img_rgb,text

iface = gr.Interface(
    fn = detect_face_and_eyes,
    inputs=gr.Image(type='pil',label='Upload an Iamge'),
    outputs=[
        gr.Image(label="Detedted Faces & Eyes"),
        gr.Text(label="Detection Result")
    ],
    title="Face & Eye Detection System",
    description="Upload an image to automatically detect faces and eyes using OpenCV"
)

iface.launch()
            