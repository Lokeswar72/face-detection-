# app.py
import streamlit as st
from ui import show_title, image_upload_ui, display_uploaded_image, display_detected_image
from logic import detect_faces

def main():
    show_title()
    uploaded_file = image_upload_ui()

    if uploaded_file:
        display_uploaded_image(uploaded_file)
        
        if st.button("🔍 Detect Faces"):
            with st.spinner("Processing..."):
                image_with_boxes, count = detect_faces(uploaded_file)
                display_detected_image(image_with_boxes, count)

if __name__ == "__main__":
    main()