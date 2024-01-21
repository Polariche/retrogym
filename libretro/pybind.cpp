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


struct PyEmulator {
    Emulator _e;
      
    bool init(const char* core_path) {
        return _e.core_load(core_path);
    }

    bool deinit() {
        _e.core_unload();
        return true;
    }

    bool load_game(const char* game_path) {
        return _e.game_load(game_path);
    }

    bool unload_game() {
        return _e.game_unload();
    }

    bool run() {
        _e.core.retro_run();
        return true;
    }

    bool reset() {
        _e.core.retro_reset();
        return true;
    }

    py::list get_keys() {
      py::list li;
      int i = 0;
      for(i=0; _e.input_desc[i].device; i++) {
        py::tuple tup = py::make_tuple(_e.input_desc[i].id, _e.input_desc[i].description);
        li.append(tup);
      }
      return li;
    }

    void set_key(int id) {
        _e.input = (int16_t) (1 << id);
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
    .def("load_game", &PyEmulator::load_game)
    .def("unload_game", &PyEmulator::unload_game)
    .def("run", &PyEmulator::run)
    .def("reset", &PyEmulator::reset)
    .def("get_keys", &PyEmulator::get_keys)
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