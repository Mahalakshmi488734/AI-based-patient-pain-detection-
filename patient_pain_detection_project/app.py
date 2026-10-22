import streamlit as st
from PIL import Image
import numpy as np
import os
import joblib

st.set_page_config(page_title="Patient Pain Detection Prototype", page_icon="🩺")
st.title("AI-Based Non-Communicative Patient Pain Detection")
st.warning(
    "Educational prototype only. Facial expressions alone cannot reliably determine pain. "
    "Do not use this app for diagnosis or clinical decisions."
)

st.write(
    "Upload an image to preview it. A trained model is not included, so this starter app "
    "does not make a real pain prediction."
)

uploaded_file = st.file_uploader("Upload a face image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)

    model_path = "pain_model.joblib"
    if os.path.exists(model_path):
        st.info(
            "A model file was found, but prediction is intentionally not enabled in this "
            "starter version. Add and validate a suitable model before enabling predictions."
        )
    else:
        st.info(
            "Image upload works. No trained model is included, so no pain level is predicted."
        )

st.caption("Prototype for learning and software engineering demonstration.")
