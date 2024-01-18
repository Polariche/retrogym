import libretro 
import numpy as np

import matplotlib.pyplot as plt
import random as rand

def group_argb8888(data):
    return np.array(data).reshape(-1,4)[:,:3]

e = libretro.Emulator()
e.init("cores/2048/2048_libretro.so")

# gently press the start button to start the game
e.set_key(1 << 3)
e.run()
e.set_key(0)

for i in range(60):

    key = rand.randint(4,7)
    
    e.set_key(1 << key)
    e.run()
    e.set_key(0)
    e.run()
    
    col = group_argb8888(e.get_video())
    data = e.get_memory_data(0)

    print(data[0])

    plt.imsave(f"screenshots/{i}.png", col.reshape(464,376,3))

e.deinit()