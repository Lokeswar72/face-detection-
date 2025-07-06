# logic.py
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import streamlit as st

def detect_faces(image_file):
    image = Image.open(image_file).convert("RGB")
    image_np = np.array(image)

    # Detect faces
    face_locations = face_recognition.face_locations(image_np)

    # Draw boxes
    draw = ImageDraw.Draw(image)
    for top, right, bottom, left in face_locations:
        draw.rectangle([left, top, right, bottom], outline="red", width=3)

    return image, len(face_locations)

def show_title():
    st.title("Face Detection App")

def image_upload_ui():
    return st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

def display_uploaded_image(uploaded_file):
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

def display_detected_image(image_with_boxes, count):
    st.image(image_with_boxes, caption=f"Detected Faces: {count}", use_container_width=True)