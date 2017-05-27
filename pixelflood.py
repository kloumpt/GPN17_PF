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
iterations = int(sys.argv[2])
path = "temp"

buffer = open(path, 'r').read().encode()

def send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))
    while True:
        #mask = iter(np.random.randint(0, 100, buffer.len()))
        sock.send(buffer)

from concurrent.futures import ThreadPoolExecutor as Pool

with Pool(cores) as pool:
    while True:
        pool.submit(send)

