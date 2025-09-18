import cv2



def rotate_image(image, angle, center=True, clockwise=True, scale=1):
    height, width, channel = image.shape
    if center == True:
        center = (width//2, height//2)
    else:
        center_x, center_y = int(input("enter center form x axis and y axis: "))
        center = (center_y, center_x)
    if clockwise != True:
        angle = angle
    else:
        angle = -angle
    
    M = cv2.getRotationMatrix2D(center=center, angle=angle, scale=scale)
    rotated_image = cv2.warpAffine(image, M=M, dsize=(width, height))

    return rotated_image

