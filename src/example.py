import libretro 
import numpy as np

import matplotlib.pyplot as plt
import random as rand

def group_argb8888(data):
    return np.array(data).reshape(-1,4)[:,:3]

def press_and_wait(key):
    e.set_key(1 << key)
    e.run()
    

e = libretro.Emulator()
e.init("cores/2048/2048_libretro.so")

# gently press the start button to start the game
data = e.get_memory_data(0)

if (data[2] == 0):
    press_and_wait(3)

print(len(data))

for i in range(10):

    key = rand.randint(4,7)
    press_and_wait(key)
    
    col = group_argb8888(e.get_video())
    data = e.get_memory_data(0)

    print(data[10::10].reshape(4,4))

    plt.imsave(f"screenshots/{i}.png", col.reshape(464,376,3))

    if (data[2] == 2):
        press_and_wait(3)

e.deinit()