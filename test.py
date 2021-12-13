import ktrain
import cv2

model = ktrain.load_predictor('models/')

def real_prediction(fname):
  pred = round(model.predict_filename(fname)[0])
  image = cv2.imread(fname)
  cv2.imshow('',image)
  print('Predicted age: %s' % pred)
  cv2.waitKey(0)

real_prediction('IMG-20190916-WA0000-1.jpg')