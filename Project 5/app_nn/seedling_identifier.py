import os
import pickle
import numpy as np
#import keras.preprocessing
from keras.applications import xception
from keras.preprocessing import image
from keras.models import load_model, model_from_json
import json
import cv2

#load json containing model architecture
with open('../seedlings_model.txt') as jsonfile:
    json_string = json.load(jsonfile)

#build model architecture
model = model_from_json(json_string)
#load model weights from seedling training
model.load_weights('../xception_seedlings_weights.h5')

## detect and segment plants in the image 
def create_mask_for_plant(image):
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    sensitivity = 35
    lower_hsv = np.array([60 - sensitivity, 100, 50])
    upper_hsv = np.array([60 + sensitivity, 255, 255])

    mask = cv2.inRange(image_hsv, lower_hsv, upper_hsv)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    return mask

def segment_plant(image):
    mask = create_mask_for_plant(image)
    output = cv2.bitwise_and(image, image, mask = mask)
    return output

def sharpen_image(image):
    image_blurred = cv2.GaussianBlur(image, (0, 0), 3)
    image_sharp = cv2.addWeighted(image, 1.5, image_blurred, -0.5, 0)
    return image_sharp

def read_segmented_image(filepath, img_size):
    img = cv2.imread(filepath, cv2.IMREAD_COLOR)
    img = cv2.resize(img.copy(), img_size, interpolation = cv2.INTER_AREA)

    image_mask = create_mask_for_plant(img)
    image_segmented = segment_plant(img)
    image_sharpen = sharpen_image(image_segmented)
    return img, image_mask, image_segmented, image_sharpen

def preprocess_image(img):
    img /= 255.
    img -= 0.5
    img *= 2
    return img

CATEGORIES = [['Black-grass','Weed'], ['Charlock','Weed'] , ['Cleavers','Weed'], ['Common Chickweed','Weed'], ['Common wheat','Crop'], ['Fat Hen','Weed'], ['Loose Silky-bent','Weed'],
              ['Maize','Crop'], ['Scentless Mayweed','Weed'], ['Shepherds Purse','Weed'], ['Small-flowered Cranesbill','Weed'], ['Sugar beet','Crop']]

# load xception base model and predict the last layer, resulting in 2048 neurons per image (a vectorized representation from xception)
base_model = xception.Xception(weights='imagenet', include_top=False, pooling='avg')
base_model.compile('sgd','mse')


#combine preprocessing, base model (xception) vectorization, and final prediction
def identify(filepath):

    _,_,_,img = read_segmented_image(filepath, (299,299))
    img = preprocess_image(np.expand_dims(img.copy().astype(np.float), axis=0))
    img_bf = base_model.predict(img)
    return CATEGORIES[np.argmax(model.predict(img_bf))]





if __name__ == '__main__':
    print(identify('Run with main.py'))