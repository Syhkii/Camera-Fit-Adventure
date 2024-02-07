from PIL import Image
from numpy import array
im_1 = Image.open(r"hearth.png")
ar = array(im_1)
matrix = []
colors = []
for x in ar:
    list = []
    for y in x:
        if str(y) in colors:
            list.append(colors.index(str(y))-1)
        else:
            colors.append(str(y))
            list.append(colors.index(str(y))-1)
    matrix.append(list)
for l in matrix:
    print(l,',')