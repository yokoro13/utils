from PIL import Image
from glob import glob

files = glob("./samples/*")
images = []
for f in files:
    images.append(Image.open(f))

images[0].save('pillow_imagedraw.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=1, loop=0)