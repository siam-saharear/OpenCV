import cv2



def rotate_image(image, angle, center=True, clockwise=True, scale=1):
    height, width, channel = image.shape
    if center == True:
        center = (width//2, height//2)
    else:
        center_x, center_y = map(int, input("enter center value of x and y: ").split(" "))
        center = (center_y, center_x)
    if clockwise != True:
        angle = angle
    else:
        angle = -angle
    
    M = cv2.getRotationMatrix2D(center=center, angle=angle, scale=scale)
    cos = abs(M[0, 0])
    sin = abs(M[0, 1])
    new_width = int((height * sin) + (width * cos))
    new_height = int((height * cos) + (width * sin))

    M[0, 2] += (new_width / 2) - center[0]
    M[1, 2] += (new_height / 2) - center[1]
    rotated_image = cv2.warpAffine(image, M=M, dsize=(new_width, new_height))
    return rotated_image

