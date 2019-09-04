import os
from PIL import Image
from glob import glob
from tqdm import tqdm

flist = []
fhist = []
dl = []

dirname = './sky/'

for e in ['png', 'jpg']:
    flist.extend(glob('%s/*.%s'%(dirname,e)))

for fn in tqdm(flist):
    try:
        fhist.append(Image.open(fn).histogram())
    except OSError:
        os.remove(fn)

for i in tqdm(range(len(flist))):
    if flist[i] in dl:
        continue
    for j in range(i+1, len(flist)):
        if flist[j] in dl:
            continue
        if fhist[i] == fhist[j] and not flist[j] in dl:
            dl.append(flist[j])

for a in dl:
    os.remove(a)

print(str(len(dl)) + " files is deleted")

