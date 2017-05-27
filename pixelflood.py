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
cores = int(sys.argv[1])
path = "temp"

buffer = open(path, 'r').read().encode()

def send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))
    sock.send(buffer)


from multiprocessing import Pool

with Pool(cores) as pool:
    while True:
        pool.apply_async(send)

