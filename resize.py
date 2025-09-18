import cv2
import os



def resize_image(image, new_height=None, new_width=None, resize_factor=1):
    height,width,channel = image.shape

    aspect_ratio = width/height
    if new_height != None:
        new_height = int(new_height)
        new_width = int(aspect_ratio*new_height)
    elif new_width != None:
        new_width = int(new_width) 
        new_height = int(aspect_ratio/height)   
    elif resize_factor != 1:
        new_height = height*resize_factor
        new_width = width*resize_factor
    else:
        print("INVALID DATA")
        
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image