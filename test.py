import ktrain
import cv2
import numpy as np
import PIL.Image as Image

model = ktrain.load_predictor("models/")


def real_prediction(fname):
    files = Image.open(fname)
    image_array = np.array(files.convert("RGB"))
    # pred = model.predict(image_array)
    # image = cv2.imread(files)
    # cv2.imshow("", files)
    # print("Predicted age: %s" % pred)
    # cv2.waitKey(0)
    print(image_array.shape)


real_prediction("IMG-20190916-WA0000-1.jpg")
