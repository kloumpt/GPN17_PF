#!/usr/bin/env python2
import random, socket
import subprocess
import sys
import time
import os
from PIL import Image
import threading

import numpy as np

MAXH = 1920
MAXW = 1200
xoffset = int(sys.argv[2])
yoffset = int(sys.argv[3])
iterations = 10
path = "temp"

def pixel(myfile, x, y, r, g, b, a=255):
        if a == 255:
            return ('PX %d %d %02x%02x%02x\n' % (x, y, r, g, b))
        elif a > 0:
            return ('PX %d %d %02x%02x%02x%02x\n' % (x, y, r, g, b, a))

def calculate(xoffset, yoffset, image, w, h):
    with open(path, "a") as myfile:
        buffer=''
        for x in range(w):
            for y in range(h):
                print(x, '/', w, y, '/', h)
                r, g, b, a = image.getpixel((x, y))
                buffer += pixel(myfile, x + xoffset, y + yoffset, r, g, b, a)
        myfile.write(buffer)

image = Image.open(sys.argv[1]).convert('RGBA')

if os.path.isfile(path):
    os.unlink(path)

_, _, w, h = image.getbbox()
for i in range(iterations):
    calculate(xoffset, yoffset, image, w, h)

