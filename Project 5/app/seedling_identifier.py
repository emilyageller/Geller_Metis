import os
import pickle
import numpy as np
#import keras.preprocessing
from keras.applications import xception
from keras.preprocessing import image
from keras.models import load_model

xception_bottleneck = load_model('/Users/emilygeller/ds/metis/metisgh/Geller_Metis/Project 5/xception_bottleneck.h5')
logreg = pickle.load( open( "/Users/emilygeller/ds/metis/metisgh/Geller_Metis/Project 5/logreg.p", "rb" ))

CATEGORIES = ['Black-grass', 'Charlock', 'Cleavers', 'Common Chickweed', 'Common wheat', 'Fat Hen', 'Loose Silky-bent',
              'Maize', 'Scentless Mayweed', 'Shepherds Purse', 'Small-flowered Cranesbill', 'Sugar beet']

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
    print(identify('/Users/emilygeller/ds/metis/metisgh/Geller_Metis/Project 5/data/test/0a64e3e6c.png'))