from PIL import Image
import cv2
import numpy as np

def remove_v1(image_path, remove_height):
    # Open the image
    img = Image.open(image_path)
    
    # Remove the top part of the image
    img_cropped = img.crop((0, remove_height, img.width, img.height))
    
    # Save the cropped image
    img_cropped.save("cut.png")

def remove_v2(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Threshold the image to obtain binary image
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Get the bounding box of the largest contour
    if contours:
        x, y, w, h = cv2.boundingRect(contours[0])
        
        # Remove the white rectangle from the image
        img_cropped = img[y+h:, :]
        
        # Save the cropped image
        cv2.imwrite("cut2.png", img_cropped)
        
        return h


# remove_v1("test.png", 100)
remove_v2("cut.png")
