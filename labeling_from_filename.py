import os
import glob
import numpy as np
from tqdm import tqdm


def write_tags(img_name, labels):
    attr_file.write(img_name)

    for label in labels:
        attr_file.write(" " + str(label))
    attr_file.write("\n")


def create_new_file():
    dir_name = "./interior"
    dir_list = os.listdir(dir_name)

    print(dir_list)
    i = 0

    label_names = ["black_floor", "red_brick_wall", "white_floor", "white_wall", "wood_floor", "wood_wall"]

    for label in dir_list:
        file = glob.glob(dir_name + "/" + label + "/*")
        labels = []
        for l in label_names:
            if l == label:
                labels.append(1)
            else:
                labels.append(0)

        for img in file:
            file_name = "{0:05d}.jpg".format(i)
            write_tags(file_name, labels)
            os.rename(img, "./indoor/" + file_name)
            i += 1

def add_new_files():
    files = os.listdir("./img_dir")
    write_file = open("test2.txt", "a")

    for file_name in tqdm(files):
        write_file.write(file_name)
        write_file.write(" 0 0 0 0 0 0 0 1")
        write_file.write("\n")
    write_file.close()

if __name__ == '__main__':
    attr_file = open("./attr_interior.txt", "a")
    attr_file.close()

    add_new_files()
