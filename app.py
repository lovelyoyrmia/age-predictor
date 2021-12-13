import streamlit as st
import ktrain
import cv2
from PIL import Image

model = ktrain.load_predictor("models/")


def real_prediction(fname):
    pred = round(model.predict_filename(fname)[0])
    image = cv2.imread(fname)
    cv2.imshow("", image)
    print("Predicted age: %s" % pred)
    cv2.waitKey(0)


st.title("Age Detection")


@st.cache()
def load_image(image):
    image_load = Image.open(image)
    return image_load


image_upload = st.file_uploader("Pick Your Image", type=["jpg", "jpeg", "png"])

if image_upload:
    image = load_image(image_upload)
    st.image(image)
