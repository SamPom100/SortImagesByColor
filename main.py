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

if not os.path.exists('input'):
    os.makedirs('input')

if not os.path.exists('output'):
    os.makedirs('output')

for item in COLORS:
    if not os.path.exists('output/'+item):
        os.makedirs('output/'+item)

path, dirs, files = next(os.walk('input/'))

file_count = len(files)
count = 1

for filename in glob.glob('input/*'):
    try:
        im = Image.open(filename)
        temp = getDominantColor(im, str(filename[8:]))
        print('('+str(count)+'/'+str(file_count)+') , '+temp)
        count = count+1
    except:
        print(str(filename) + ' is not an image')
