from PIL import Image, ImageChops
import os

# Image directory
origin_dir = 'origin'
cropped_dir = 'cropped'

def crop(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    gray = img.convert('L')

    # Determine the size of the white frame on the top and bottom
    top_frame_height = 0
    bottom_frame_height = gray.height

    # Loop through the top side to determine the height of the white frame
    for y in range(gray.height):
        if all(gray.getpixel((x, y)) == 255 for x in range(gray.width)):
            top_frame_height += 1
        else:
            break

    # Loop through the bottom side to determine the height of white frame
    for y in range(gray.height - 1, -1, -1):
        if all(gray.getpixel((x, y)) == 255 for x in range(gray.width)):
            bottom_frame_height -= 1
        else:
            break

    # Crop the image to remove the top and bottom white frames
    return img.crop((0, top_frame_height, img.width, bottom_frame_height))


def process():
    for img_file in os.listdir(origin_dir):
        f = os.path.join(origin_dir, img_file)
        
        if os.path.isfile(f):
            if f.lower().endswith('.png'):
                cropped = crop(f)
                cropped.save(cropped_dir + '/' + img_file)

process()