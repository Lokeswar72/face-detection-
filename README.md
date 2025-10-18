# face detection Streamlit

![image](https://github.com/user-attachments/assets/dfac929a-b406-4a34-84a3-595c685d1e6c)

# Face Detection AI

A simple web application built with Streamlit to detect faces in an uploaded image. This app is CPU-friendly and uses the `face_recognition` library.

!Face Detection App Screenshot
*(Suggestion: Add a screenshot of your app here)*

## Features

- Upload an image (JPG, JPEG, PNG).
- Display the uploaded image.
- Detect faces in the image upon clicking a button.
- Display the image with bounding boxes around detected faces.
- Show a count of the detected faces.

## Project Structure

```
ai_projectss/
├── app.py          # Main Streamlit application
├── logic.py        # Core face detection logic
├── ui.py           # Streamlit UI components
├── requirements.txt # Python dependencies
└── README.md       # This file
```

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd ai_projectss
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    # On Windows
    .\env\Scripts\activate
    # On macOS/Linux
    source env/bin/activate
    ```

3.  **Install the dependencies:**
    This project requires `dlib` which can have a complex installation. It's recommended to install it first.
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

Once the setup is complete, run the Streamlit app with the following command:

```bash
streamlit run app.py
```

This will open the application in your default web browser.
