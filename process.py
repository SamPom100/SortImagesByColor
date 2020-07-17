from __future__ import print_function
from math import sqrt
import binascii
import struct
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
import matplotlib.pyplot as plt
import matplotlib.colors as mc
import webcolors


NUM_CLUSTERS = 5


def getDominantColor(img, filename):
    try:
        im = img.resize((100, 100))
        ar = np.asarray(im)
        shape = ar.shape
        ar = ar.reshape(np.product(shape[:2]), shape[2]).astype(float)
        codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
        vecs, dist = scipy.cluster.vq.vq(ar, codes)
        counts, bins = np.histogram(vecs, len(codes))
        index_max = np.argmax(counts)
        peak = codes[index_max]
        color = binascii.hexlify(bytearray(int(c)
                                           for c in peak)).decode('ascii')
        rgb = ImageColor.getcolor('#'+color, "RGB")
        colorName = get_closest_color(rgb)
        img.save('output/'+colorName+'/'+filename, 'PNG')
        return(filename + ' is '+colorName)
    except:
        print(filename + ' was broken')


def debug(rgb, img):
    tempIMG = Image.new('RGB', (500, 500), color=rgb)
    draw = ImageDraw.Draw(tempIMG)
    colorName = get_closest_color(rgb)
    text = colorName + str(rgb)
    draw.text((0, 0), text, (255, 255, 255))
    toShow = get_concat_h(tempIMG, img.resize(
        (500, 500))).show()


def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst


COLORS = (
    (255, 0, 0),  # red
    (255, 125, 0),  # orange
    (255, 255, 0),  # yellow
    (125, 255, 0),  # spring green
    (0, 255, 0),  # green
    (0, 255, 125),  # turquoise
    (0, 0, 255),  # cyan
    (0, 125, 255),  # ocean
    (0, 0, 255),  # blue
    (125, 0, 255),  # violet
    (255, 0, 255),  # magenta
    (255, 0, 125),  # raspberry
    (-50, -50, -50,),  # black
    (300, 300, 300),  # white
)

COLOR_NAMES = {
    (255, 0, 0): "red",
    (255, 125, 0):  "orange",
    (255, 255, 0):  "yellow",
    (125, 255, 0):  "spring green",
    (0, 255, 0):  "green",
    (0, 255, 125):  "turquoise",
    (0, 0, 255):  "cyan",
    (0, 125, 255):  "ocean",
    (0, 0, 255):  "blue",
    (125, 0, 255):  "violet",
    (255, 0, 255):  "magenta",
    (255, 0, 125):  "raspberry",
    (-50, -50, -50):  "black",
    (300, 300, 300):  "white",
}


def get_closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return COLOR_NAMES.get(min(color_diffs)[1])


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
