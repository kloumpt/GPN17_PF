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

buffer = open(path, 'r').read()

def send():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST,PORT))
        while True:
            #mask = iter(np.random.randint(0, 100, buffer.len()))
            try:
                sock.send(buffer)
            except Exception:
                return

from concurrent.futures import ThreadPoolExecutor as Pool

tmp_buffer = ''
while len(tmp_buffer) < 50 * 10**6:
    tmp_buffer += buffer

buffer = tmp_buffer.encode()

with Pool(cores) as pool:
    while True:
        pool.submit(send)

