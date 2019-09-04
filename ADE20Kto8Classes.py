import numpy as np
from PIL import Image
import os
from tqdm import tqdm
import cv2

ade_path = '../../Documents/ADEChallengeData2016/annotations/'

an_path = os.listdir(ade_path)

img_dir = os.listdir(ade_path + "validation")
for img_path in tqdm(img_dir):
    img_path_ = os.path.join('../../Documents/ADEChallengeData2016/annotations/validation', img_path)
    img = Image.open(img_path_)
    img = np.asarray(img)
    img = np.where((img != 1) & (img != 2), 0, 1) + \
          np.where((img != 4) & (img != 7) & (img != 14) & (img != 29), 0, 2) + \
          np.where(img != 6, 0, 3) + \
          np.where((img != 16) & (img != 34), 0, 4) + \
          np.where(img != 19, 0, 5) + \
          np.where((img != 20) & (img != 32) & (img != 70) & (img != 76), 0, 6) + \
          np.where(img != 25, 0, 7)

    img = Image.fromarray(img)
    img.save('../../Documents/ADEChallengeData2016/annotations/validation' + "5c/" + img_path)

"""
img = Image.open("./1.png")
img = np.asarray(img)
print(img)

print(img)
img = Image.fromarray(img)
img.save("4.png")"""
