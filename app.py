import os

import streamlit as st
import ktrain
import cv2
import io
from PIL import Image

model = ktrain.load_predictor("models/")


def real_prediction(fname, model):
    pred = round(model.predict_filename(fname)[0])
    return pred


st.title("Age Detection")


@st.cache()
def load_image(image):
    image_load = Image.open(image)
    return image_load


def load_imgpath(image_path):
    try:
        with open(os.path.join("uploads", image_path.name), "wb") as f:
            f.write(image_path.getbuffer())
        return 1
    except:
        return 0


image_upload = st.file_uploader("Pick Your Image", type=["jpg", "jpeg", "png"])

if image_upload is not None:
    if load_image(image_upload):
        image = load_image(image_upload)
        st.image(image)
        # buf = io.BytesIO()
        # image.save(buf, "JPEG")
        # img_bytes = buf.getvalue()
        pred = real_prediction(os.path.join("uploads", image_upload.name), model)
        st.subheader(f"Predicted age {pred} year old")
