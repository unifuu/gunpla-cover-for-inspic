import cv2

# Read the image
image = cv2.imread('origin.png')

# Assume we have already detected the object and obtained its coordinates
x = 0  # top-left x-coordinate
y = 0  # top-left y-coordinate
w = 1920  # width of the rectangle
h = 200  # height of the rectangle

# Draw the bounding rectangle on the image
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with the bounding rectangle
cv2.imshow('Bounding Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()