import libretro 
import numpy as np

import matplotlib.pyplot as plt


def group_argb8888(data):
    return np.array(data).reshape(-1,4)[:,:3]

e = libretro.Emulator()
e.init("cores/2048/2048_libretro.so")
e.set_key(1 << 3)

for _ in range(60):
    e.run()
    col = group_argb8888(e.get_video())
    plt.imsave("sdf.png", col.reshape(464,376,3))

e.deinit()