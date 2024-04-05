from PIL import Image, ImageChops

def remove_white_background(image_path):
    # Load the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    img_gray = img.convert('L')

    # Determine the size of the white frame on the top and bottom
    top_frame_height = 0
    bottom_frame_height = img_gray.height

    # Loop through the top side to determine the height of the white frame
    for y in range(img_gray.height):
        if all(img_gray.getpixel((x, y)) == 255 for x in range(img_gray.width)):
            top_frame_height += 1
        else:
            break

    # Loop through the bottom side to determine the height of the white frame
    for y in range(img_gray.height - 1, -1, -1):
        if all(img_gray.getpixel((x, y)) == 255 for x in range(img_gray.width)):
            bottom_frame_height -= 1
        else:
            break

    # Crop the image to remove the top and bottom white backgrounds
    img_cropped = img.crop((0, top_frame_height, img.width, bottom_frame_height))

    # Save or display the resulting image
    img_cropped.show()
    # img_cropped.save('cropped_image.png')

# Example usage:
remove_white_background('origin.png')