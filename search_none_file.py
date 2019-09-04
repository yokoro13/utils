import os

path = "C:/Users/nishimura-VR-02/Documents/stargan-master/data/interior/images"

files = os.listdir(path)

files_ = os.listdir("./indoor")
set_ab = set(files) - set(files_)
list_ab = list(set_ab)

list_ab.sort()

#for a in list_ab:
#    print(a)

lines = [line.rstrip() for line in open("./attr_interior.txt", 'r')]
all_attr_names = lines[1].split()

lines = lines[2:]
filename = []
for i, line in enumerate(lines):
    split = line.split()
    filename.append(split[0])

set_ab = set(filename) - set(files_)
list_ab = list(set_ab)

list_ab.sort()
for a in list_ab:
    print(a)
