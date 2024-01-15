#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include "emulator.h"

PYBIND11_MODULE(retro, m) {
    /*
    m.def("core_load", &core_load, "");
    m.def("core_unload", &core_unload, "");
    m.def("core_load_game", &core_load_game, "");

    m.def("audio_init", &audio_init, "");
    m.def("video_configure", &video_configure, "");

    m.def("audio_deinit", &audio_deinit, "");
    m.def("video_deinit", &video_deinit, "");

    m.def("retro_run", &_retro_run, "");
    m.def("retro_reset", &_retro_reset, "");
    m.def("retro_load_game", &_retro_load_game, "");
    m.def("retro_unload_game", &_retro_unload_game, "");
    m.def("retro_get_memory_data", &_retro_get_memory_data, "");
    m.def("retro_get_memory_size", &_retro_get_memory_size, "");

    m.def("get_video_data", &get_video_data,  "");

    m.def("puts", &puts, R"pbdoc(
        Puts
    )pbdoc");
    */
#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}