import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import glob
import os

class MainWindow(object):
    def __init__(self):
        root = tk.Tk()
        root.geometry('400x400')

        self.frame2 = tk.Frame(root)
        self.frame2.pack(side=BOTTOM)
        self.frame1 = tk.Frame(root)
        self.frame1.pack(side=BOTTOM)
        self.frame_img = tk.Frame(root)
        self.frame_img.pack(side=BOTTOM)

        self.current_image_index = 1105

        self.c_trg_labels = ["wood_floor", "marble_floor", "carpet",
                             "wood_wall", "brick_wall", "white_wall",
                             "wood_ceiling", "white_ceiling"]

        self.c_trg_tag = [-1 for i in range(len(self.c_trg_labels))]
        self.imgs = {}

        self.load_files()

        # loader
        self.label_button = []
        self.load_button = tk.Button(self.frame1, text="next", command=lambda: self.next_image())
        self.load_button.grid(row=1, column=5)

        self.label_button = []
        self.load_button = tk.Button(self.frame1, text="delete", command=lambda: self.delete_image())
        self.load_button.grid(row=1, column=3)

        self.label_button = []
        self.load_button = tk.Button(self.frame1, text="prev", command=lambda: self.prev_image())
        self.load_button.grid(row=1, column=1)

        for i, label in enumerate(self.c_trg_labels):
            self.label_button.append(tk.Button(self.frame2, text=label + "\n{}".format(self.c_trg_tag[i]), command=self.change_c_trg(i)))
            self.label_button[i].pack(side=LEFT)

        root.mainloop()

    def load_files(self):
        self.files = glob.glob("./images/*")

    def next_image(self):
        print("next")
        # self.write_tags()
        if self.current_image_index < len(self.files):
            self.current_image_index += 1
        self.load_image()

    def prev_image(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
        self.load_image()

    def delete_image(self):
        # os.remove(self.files[self.current_image_index])
        self.load_files()
        self.load_image()

    def load_image(self):
        self.imgs.clear()
        self.initialize_tags()
        self.print_tag()
        self.show_image = Image.open(self.files[self.current_image_index])
        self.print_load_image()

    def destroy_child(self, frame):
        children = frame.winfo_children()
        for child in children:
            child.destroy()

    def initialize_tags(self):
        self.c_trg_tag = [-1, -1, -1, -1, -1, -1, -1, -1]

    def get_file_name(self):
        print(self.current_image_index)
        return self.files[self.current_image_index].split("\\")[-1]

    def write_tags(self):
        attr_file = open("./list_attr_interior.txt", "a")
        attr_file.write(self.get_file_name())
        for tag in self.c_trg_tag:
            attr_file.write(" " + str(tag))
        attr_file.write("\n")
        attr_file.close()

    def read_line(self, file_name):
        file = open("./list_attr_interior.txt", "r")
        for row in file:
            if row.find(file_name) != -1:
                tmp_list.append(write1)

    def print_load_image(self):
        self.destroy_child(self.frame_img)
        w, h = self.show_image.size
        WIDTH = 512
        self.show_image = self.show_image.resize((WIDTH, int(h * WIDTH/w)))

        canvas = tk.Canvas(self.frame_img, width=WIDTH, height=h * WIDTH/w)
        canvas.place(x=100, y=350)
        self.imgs[0] = ImageTk.PhotoImage(self.show_image)
        canvas.create_image(3, 3, image=self.imgs[0], anchor=tk.NW)
        canvas.grid(row=0, column=0)

    def change_c_trg(self, index):
        def x():
            self.c_trg_tag[index] = 1 if self.c_trg_tag[index] == -1 else -1
            self.print_tag()
        return x

    def print_tag(self):
        for index in range(len(self.label_button)):
            self.label_button[index]["text"] = self.c_trg_labels[index] + "\n{}".format(self.c_trg_tag[index])


if __name__ == "__main__":
    MainWindow()
