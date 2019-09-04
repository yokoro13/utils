import glob
from tqdm import tqdm
import os

img_dir = glob.glob("./sky/*")
offset = 24921
i = offset
for img in tqdm(img_dir):
    os.rename(img, "./img_dir/" + "{0:05d}.jpg".format(i))
    i += 1
