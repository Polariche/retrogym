import libretro 
import numpy as np

import matplotlib.pyplot as plt
import random as rand

import cv2 
import time

def group_argb565(data):
    data = np.array(data).reshape(-1)
    
    r = (data & 0xF800) >> 8
    g = (data & 0x07E0) >> 3
    b = (data & 0x001F) << 3

    return np.stack([r,g,b], axis=1)

e = libretro.Emulator()
e.init("cores/mgba_libretro.so")
e.load_game("roms/pokemon_red.gb")

h = e.height()
w = e.width()

keys =  e.get_keys()

while True:
    for i, _ in keys:
        e.set_key(i, False)
    cur_key = rand.choice(keys)
    e.set_key(cur_key[0], True)
    
    e.run()
    time.sleep(0.01)

    data = e.get_memory_data(2)
    # print(data)

    #print(data[0xC104], data[0xC106])

    col = group_argb565(e.get_video()).reshape(h,w,3).astype(np.uint8) #group_argb8888(e.get_video()).reshape(h,w,3)
    cv2.imshow('', col)
    cv2.waitKey(1)

    