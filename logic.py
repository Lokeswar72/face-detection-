# ui.py
import streamlit as st
from PIL import Image
import numpy as np
import face_recognition
from PIL import Image, ImageDraw

def show_title():
    st.set_page_config(page_title="Face Detection AI", layout="centered")
    st.title("🧠 Advanced Face Detection (CPU Friendly)")

def image_upload_ui():
    return st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

def display_uploaded_image(image):
    st.image(image, caption="Uploaded Image", use_container_width=True)

def display_detected_image(image, count):
    st.success(f"✅ Detected {count} face(s)")
    st.image(image, caption="Processed Image", use_container_width=True)

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