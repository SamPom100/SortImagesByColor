from PIL import Image
import glob
from process import getDominantColor
import os

COLORS = [
    "red",
    "orange",
    "yellow",
    "spring green",
    "green",
    "turquoise",
    "cyan",
    "ocean",
    "blue",
    "violet",
    "magenta",
    "raspberry",
    "black",
    "white",
]

if not os.path.exists('process'):
    os.makedirs('process')

if not os.path.exists('output'):
    os.makedirs('output')

for item in COLORS:
    if not os.path.exists('output/'+item):
        os.makedirs('output/'+item)

for filename in glob.glob('process/*'):
    try:
        im = Image.open(filename)
        getDominantColor(im, str(filename[8:]))
    except:
        print(str(filename) + ' is not an image')


"""
purple = (138, 43, 226)

black = (-50, -50, -50)

violet = (125, 0, 255)

image = (92, 67, 98)


def helper(name, name2):
    r, g, b = name
    cr, cg, cb = name2
    color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
    return color_diff


print(helper(image, black))
print(helper(image, violet))
print(helper(image, purple))`
"""
