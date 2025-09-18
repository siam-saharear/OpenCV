import os
import cv2

def image_options(current_directory=True, image_folder=None):
    current_directory_path = os.getcwd()
    all_images = []
    
    if current_directory == True:
        image_folder_path = current_directory_path
    else: 
        image_folder_path = os.path.join(current_directory, image_folder)
    
    if len(os.listdir(image_folder_path)) != 0:
        for file in os.listdir(image_folder_path):
            if file.split(".")[-1] in ("png", "jpg", "tiff"):
                current_file_path = os.path.join(image_folder_path, file)
                all_images.append(current_file_path)
            else:
                print(f"file not image '{file}' ")
    else:
        print("directory empty")
    return all_images
    


