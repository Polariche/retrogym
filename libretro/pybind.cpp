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
    Emulator emu;
    py::list li;

    bool init(const char* core_path) {
        return emu.core_load(core_path);
    }

    bool deinit() {
        emu.core_unload();
        return true;
    }

    bool load_game(const char* game_path) {
        if (!emu.game_load(game_path))
            return false;
        
        for(auto & t : emu.input_desc) {
            py::tuple tup = py::make_tuple(t.id, t.description);
            li.append(tup);
        }

        return true;
    }

    bool unload_game() {
        return emu.game_unload();
    }

    bool load_save() {
        return true;
    }

    bool unload_save() {
        return true;
    }

    bool run() {
        emu.core.retro_run();
        return true;
    }

    bool reset() {
        emu.core.retro_reset();
        return true;
    }

    int width() {
        return emu.width;
    }

    int height() {
        return emu.height;
    }

    py::list get_keys() {
        return li;
    }

    void set_key(int id, bool value) {
        emu.input[id] = value;
    }

    py::array_t<uint16_t> get_video() {
        int w = emu.width;
        int h = emu.height;

        py::array_t<uint16_t> arr({ w*h } );

        switch(emu.pixel_format) {
            case RETRO_PIXEL_FORMAT_RGB565:
                uint16_t* data = arr.mutable_data();
                memcpy(data, emu.video_data, w*h*sizeof(uint16_t));
                break;
            default:
                return arr;
        }

        return arr;
    } 

    size_t get_memory_size(unsigned id) {
        return (size_t) emu.core.retro_get_memory_size(id);
    }

    py::array_t<uint8_t> get_memory_data(unsigned id) {
        size_t size = emu.core.retro_get_memory_size(id);
		py::array_t<uint8_t> arr({ (py::ssize_t) (size / sizeof(uint8_t)) });

        memcpy(arr.mutable_data(), emu.core.retro_get_memory_data(id), size);

        return arr;
    }
    
};


PYBIND11_MODULE(libretro, m) {
    py::class_<PyEmulator>(m, "Emulator")
    .def(py::init())
    .def("init", &PyEmulator::init)
    .def("deinit", &PyEmulator::deinit)
    .def("width", &PyEmulator::width)
    .def("height", &PyEmulator::height)
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