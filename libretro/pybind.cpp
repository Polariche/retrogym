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

    uint8_t get_memory_size(unsigned id) {
        return (uint8_t) _e.core.retro_get_memory_size(id);
    }

    py::array_t<int> get_memory_data(unsigned id, unsigned addr) {
		py::array_t<int> arr({ 16 });
        int* data = arr.mutable_data();
        void* mem_data = _e.core.retro_get_memory_data(id);

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