from PIL import Image, ImageChops
import os

origin_dir = 'origin'
trimmed_dir = 'trimmed'

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def loop():
    for img_file in os.listdir(origin_dir):
        f = os.path.join(origin_dir, img_file)
        
        if os.path.isfile(f):
            if f.lower().endswith('.png'):
                im = Image.open(f)
                im = trim(im)
                im.save(trimmed_dir + '/' + img_file)

loop()