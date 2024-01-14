import libretro 

libretro.core_load("cores/2048/2048_libretro.so")
libretro.puts("Core loaded")
libretro.retro_run()
libretro.core_unload()
libretro.puts("Core unloaded")