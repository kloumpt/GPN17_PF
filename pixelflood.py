#!/usr/bin/env python2
import random, socket
import subprocess
import sys
import time
import os
from PIL import Image
import threading

HOST = '94.45.231.39'
PORT = 1234
MAXH = 1920
MAXW = 1200
xoffset = int(sys.argv[2])
yoffset = int(sys.argv[3])
cores = int(sys.argv[4])
threads = []
iterations = 24
path = "temp"

def pixel(myfile, x, y, r, g, b, a=255):
        if a == 255:
            myfile.write('PX %d %d %02x%02x%02x\n' % (x, y, r, g, b))
        elif a > 0:
            myfile.write('PX %d %d %02x%02x%02x%02x\n' % (x, y, r, g, b, a))

def calculate(xoffset, yoffset, image, w, h):
    with open(path, "a") as myfile:
        for x in range(w):
            for y in range(h):
                r, g, b, a = image.getpixel((x, y))
                pixel(myfile, x + xoffset, y + yoffset, r, g, b, a)

def send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))
    with open("temp", "r") as myfile:
        sock.send(myfile.read().encode())

image = Image.open(sys.argv[1]).convert('RGBA')

if os.path.isfile(path):
    os.unlink(path)

_, _, w, h = image.getbbox()
for i in range(iterations):
    calculate(xoffset, yoffset, image, w, h)


from multiprocessing import Pool

with Pool(cores) as pool:
    while True:
        pool.apply_async(send)

