#-------------------------------------------------------------------------------
# Libraries
#-------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import pickle
import cv2
from PIL import Image

filename = '../models/x-ray_model.pkl'
model = pickle.load(open(filename, 'rb'))
img_size = 150

def x_ray_classifier(chosen_image):

    #img_arr = cv2.imread(chosen_image, cv2.IMREAD_GRAYSCALE)
    #resized_arr = cv2.resize(img_arr, (img_size, img_size)).astype('float32') # Reshaping images to preferred size
    #resized_arr = np.array(resized_arr)
    chosen_image.load()
    data = np.asarray(chosen_image, dtype="int32" )
    data = cv2.resize(data.astype(float), (img_size, img_size))
    test_image = data/255
    test_image = test_image.reshape(-1, img_size, img_size, 1)
    prediction = model.predict(test_image)
    return prediction
