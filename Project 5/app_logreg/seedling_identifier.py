import os
import pickle
import numpy as np
#import keras.preprocessing
from keras.applications import xception
from keras.preprocessing import image
from keras.models import load_model

xception_bottleneck = load_model('../xception_bottleneck.h5')
logreg = pickle.load( open( "../logreg.p", "rb" ))

CATEGORIES = [['Black-grass','Weed'], ['Charlock','Weed'] , ['Cleavers','Weed'], ['Common Chickweed','Weed'], ['Common wheat','Crop'], ['Fat Hen','Weed'], ['Loose Silky-bent','Weed'],
              ['Maize','Crop'], ['Scentless Mayweed','Weed'], ['Shepherds Purse','Weed'], ['Small-flowered Cranesbill','Weed'], ['Sugar beet','Crop']]

def read_img(filepath, size):
    img = image.load_img(filepath, target_size=size)
    img = image.img_to_array(img)
    return img

def identify(filepath):

    img = read_img(filepath, (299,299))
    x = xception.preprocess_input(np.expand_dims(img.copy(), axis = 0))
    x_bottleneck = xception_bottleneck.predict(x, verbose = 1)
    pred = logreg.predict(x_bottleneck)
    return CATEGORIES[pred[0]]


if __name__ == '__main__':
    print(identify('Run with main.py'))