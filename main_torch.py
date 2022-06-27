# Here we are gonna 
# - see what super resolution is
# - understand steps to upscale an image
# - se ebest model; found so far ()
# - conclusions
# #

import os

# import the necessary packages
import argparse
import time
import cv2
import matplotlib.pyplot as plt
import numpy as np

from super_image import EdsrModel, ImageLoader
from PIL import Image

if __name__=='__main__':

    'another way to get the input sample image'
    # img = cv2.imread("aa.png")

    # change with your image path
    input_img = "images/aa.png" 

    user_scale = 4

    image = Image.open(input_img)
    img = ImageLoader.load_image(image)
    original_img = cv2.imread(input_img)
    cv2.imshow('small image -- original', original_img)
    cv2.waitKey(1000)

    # compute the upsample image with model EDSR with chosen user_scale
    model = EdsrModel.from_pretrained('eugenesiow/edsr-base', scale=user_scale) 
    preds = model(img)
    # save and then show the upsampled image with superResolution
    ImageLoader.save_image(preds, 'images/scaled_2x.png')  
    ris  = cv2.imread('images/scaled_2x.png')
    cv2.imshow('superResolution image', ris)
    cv2.waitKey(1000)

    # compute and show reisized upsampled image
    resized = cv2.resize(original_img,dsize=None,fx=user_scale,fy=user_scale)
    cv2.imshow('upsampled original -- resizing', resized)
    cv2.waitKey(1000)

    # plot differences from superResolution image and resized image
    diff = abs(np.array(ris) - np.array(resized))
    cv2.imshow('diff', diff)
    cv2.waitKey(0)

    a=1

    print('end')