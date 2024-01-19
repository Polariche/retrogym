#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <stdbool.h>
#include <errno.h>
#include <dlfcn.h>

#include "emulator.h"

namespace py = pybind11;

typedef struct
{
   int up;
   int down;
   int left;
   int right;
   int start;
   int select;
} key_state_t;

typedef enum
{
   DIR_NONE,
   DIR_UP,
   DIR_RIGHT,
   DIR_DOWN,
   DIR_LEFT
} direction_t;

typedef enum
{
   STATE_TITLE,
   STATE_PLAYING,
   STATE_GAME_OVER,
   STATE_WON,
   STATE_PAUSED
} game_state_t;


typedef struct vector
{
   int x;
   int y;
} vector_t;

typedef struct cell {
   int value;
   vector_t pos;
   vector_t old_pos;
   float move_time;
   float appear_time;
   struct cell *source;
} cell_t;

typedef struct game {
   int score;
   int best_score;
   game_state_t state;
   key_state_t old_ks;
   direction_t direction;
   cell_t grid[16];
} game_t;

struct PyEmulator {
    Emulator _e;
      
    bool init(const char* core_path) {
        return _e.core_load(core_path);
    }

    bool deinit() {
        _e.core_unload();
        return true;
    }

    bool run() {
        _e.core.retro_run();
        return true;
    }

    bool reset() {
        _e.core.retro_reset();
        return true;
    }

    void set_key(int input) {
        _e.input = (int16_t) input;
    }

    py::array_t<uint8_t> get_video() {
        long w = 376;
		long h = 464;

		py::array_t<uint8_t> arr({ h*w*4 } );
		uint8_t* data = arr.mutable_data();

        memcpy(data, _e.video_data, h*w*4*sizeof(uint8_t));
        return arr;
    } 

    size_t get_memory_size(unsigned id) {
        return (size_t) _e.core.retro_get_memory_size(id);
    }

    py::array_t<int> get_memory_data(unsigned id) {
        size_t size = get_memory_size(id);
		py::array_t<int> arr({ size/sizeof(int) });

        int* data = arr.mutable_data();
        void* mem_data = _e.core.retro_get_memory_data(id);

        memcpy(data, mem_data, size);

        return arr;
    }

};


PYBIND11_MODULE(libretro, m) {
    py::class_<PyEmulator>(m, "Emulator")
    .def(py::init())
    .def("init", &PyEmulator::init)
    .def("deinit", &PyEmulator::deinit)
    .def("run", &PyEmulator::run)
    .def("reset", &PyEmulator::reset)
    .def("set_key", &PyEmulator::set_key)
    .def("get_video", &PyEmulator::get_video)
    .def("get_memory_size", &PyEmulator::get_memory_size)
    .def("get_memory_data", &PyEmulator::get_memory_data);
    
#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}