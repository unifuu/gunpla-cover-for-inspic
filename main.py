from PIL import Image, ImageChops
import cv2
import numpy as np
import datetime

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
    write_image(gray)
    
    # Threshold the image to obtain binary image
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(contours)
    
    # Get the bounding box of the largest contour
    if contours:
        x, y, w, h = cv2.boundingRect(contours[0])

        print(x, y, w, h)
        
        # Remove the white rectangle from the image
        img_cropped = img[y+h:, :]

        print(img_cropped)
        
        # Save the cropped image
        cv2.imwrite("new.png", img_cropped)
        
        return h

def show_image(img):
    scale_percent = 50
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    resized_image = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)

    cv2.imshow('Display image', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def write_image(img):
    cv2.imwrite("final.png", img)

def get_contours(img):
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    # thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # show_image(thresh)

    return contours

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

im = Image.open("origin.png")
im = trim(im)
im.save('trim.png')


# get_contours('test.png')

# image = cv2.imread('test.png')
# contours = get_contours('test.png')
# # print(contours)

# top_contour = min(contours, key=cv2.contourArea)
# bottom_contour = max(contours, key=cv2.contourArea)

# print(top_contour, bottom_contour)

# # Get bounding boxes
# x_top, y_top, w_top, h_top = cv2.boundingRect(top_contour)
# x_bottom, y_bottom, w_bottom, h_bottom = cv2.boundingRect(bottom_contour)

# # Crop the image to remove white borders
# cropped_image = image[y_top:y_bottom+h_bottom, 0:image.shape[1]]

# Display the cropped image
# cv2.imshow('Cropped Image', cropped_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Example usage:
# remove_v1("test.png", 100)
# remove_v2("origin.png")

################################ Test 1: Read a rectangle in the top
# img = cv2.imread('origin.png')
# x, y, w, h = 0, 100, img.shape[1], img.shape[0] - 100  # Adjust the y-coordinate and height as needed
# cropped_img = img[y:y+h, x:x+w]
# cv2.imwrite('new_cut.png', cropped_img)


############################# Test 2: Detect the white rectangle
# image = cv2.imread('origin.png')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _, binary_mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
# contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Filter contours to identify the one corresponding to the white rectangle
# for contour in contours:
#     x, y, w, h = cv2.boundingRect(contour)
#     # Assuming the white rectangle is at the top of the image
#     if y < 50:  # Adjust this threshold as needed
#         # Draw a bounding box around the detected white rectangle
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         break  # Assuming there is only one white rectangle

# # Show the image with the detected rectangle
# cv2.imshow('Detected Rectangle', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

######################################### Test 3
# # Read the image
# image = cv2.imread('origin.png')

# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Threshold the grayscale image to create a binary mask
# _, binary_mask = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

# # Find contours in the binary mask
# contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Filter contours to identify the one corresponding to the white rectangle
# for contour in contours:
#     x, y, w, h = cv2.boundingRect(contour)
#     # Assuming the white rectangle is at the top of the image
#     if y < 50:  # Adjust this threshold as needed
#         # Draw a bounding box around the detected white rectangle
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         break  # Assuming there is only one white rectangle


################################ Test 4
# image = cv2.imread('test.png')

# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Threshold the grayscale image to create a binary mask
# _, binary_mask = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

# # Find contours in the binary mask
# contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Filter contours to identify the ones corresponding to the white rectangles
# white_rectangles = []
# for contour in contours:
#     x, y, w, h = cv2.boundingRect(contour)
#     # Check if the contour is close to the image boundary
#     if x < 10 or y < 10 or x + w > image.shape[1] - 10 or y + h > image.shape[0] - 10:
#         white_rectangles.append((x, y, w, h))

# print(white_rectangles)

# # Draw bounding boxes around the detected white rectangles
# for rect in white_rectangles:
#     x, y, w, h = rect
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # image2 = Image.open('origin.png')
# # img = image2.crop((49, 49, 49, 49))
# # img.save("final2.png")

# show_image(image)
# write_image(image)
