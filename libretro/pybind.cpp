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
        return emu.init(core_path);
    }

    bool deinit() {
        emu.deinit();
        return true;
    }

    bool load_game(const char* game_path) {
        if (!emu.load_game(game_path))
            return false;
        
        std::vector<std::pair<int, std::string>> emu_keys = emu.get_keys();
        for(auto & t : emu_keys) {
            py::tuple tup = py::make_tuple(t.first, t.second);
            li.append(tup);
        }

        return true;
    }

    bool unload_game() {
        return emu.unload_game();
    }

    bool load_state(const char* state_path) {
        return emu.load_state(state_path);
    }

    bool save_state(const char* state_path) {
        return emu.save_state(state_path);
    }

    bool run() {
        return emu.run();
    }

    bool reset() {
        return emu.reset();
    }

    int width() {
        return emu.get_width();
    }

    int height() {
        return emu.get_height();
    }

    py::list get_keys() {
        return li;
    }

    void set_key(int id, bool value) {
        emu.set_key(id, value);
    }

    py::array_t<uint16_t> get_video() {
        int w = emu.get_width();
        int h = emu.get_height();

        py::array_t<uint16_t> arr({ w*h } );

        uint16_t* data = arr.mutable_data();
        memcpy(data, emu.get_video(), w*h*sizeof(uint16_t));
        return arr;
    } 

    size_t get_memory_size(unsigned id) {
        return emu.get_memory_size(id);
    }

    uint8_t get_memory_data(unsigned id, unsigned addr) {
        return emu.get_memory_data(id, addr);
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
    .def("load_state", &PyEmulator::load_state)
    .def("save_state", &PyEmulator::save_state)
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