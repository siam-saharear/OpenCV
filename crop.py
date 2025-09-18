import cv2
import os


def crop_image(image, x1, x2, y1, y2): 
    if x1<x2 and y1<y2 and x1>=0 and x2>=0:
        cropped_image = image[y1:y2, x1:x2]
    else:
        print("INVALID CORDINATION")
    if cropped_image:
        return cropped_image
    

# cropped_image = image[100:225, 300:525]