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
