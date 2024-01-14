import libretro 
from ctypes import cdll, CFUNCTYPE, POINTER, cast, memmove
from ctypes import c_bool, c_int, c_uint, c_int16, c_char_p, c_void_p, c_size_t
import ctypes
import numpy as np

from PIL import Image
import matplotlib.pyplot as plt

libretro.core_load("cores/2048/2048_libretro.so")
libretro.puts("Core loaded")

libretro.retro_run()

print(libretro.get_video_data())
plt.imsave("screenshot.png", libretro.get_video_data())

libretro.retro_reset()
libretro.core_unload()
libretro.puts("Core unloaded")