/**
 * noarch: a small libretro frontend that doesn't provide any video, audio or input.
 *
 * It loads a Core, along with its Content, runs an iteration, and then quits. This is useful for unit testing.
 *
 * License: BSD 3-Clause "New" or "Revised" License
 *
 * Copyright 2021 Rob Loach (@RobLoach)
 */
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <stdbool.h>
#include <errno.h>
#include <dlfcn.h>

#include "libretro.h"

namespace py = pybind11;

int width = 0;
int height = 0;
void* video_data;

static struct {
  void * handle;
  bool initialized;

  const void* video_data = nullptr;
  size_t video_pitch = 0;

  void (*retro_init)(void);
  void (*retro_deinit)(void);
  unsigned (*retro_api_version)(void);
  void (*retro_get_system_info)(struct retro_system_info* info);
  void (*retro_get_system_av_info)(struct retro_system_av_info* info);
  void (*retro_set_controller_port_device)(unsigned port, unsigned device);
  void (*retro_reset)(void);
  void (*retro_run)(void);
  size_t (*retro_serialize_size)(void);
  bool (*retro_serialize)(void *data, size_t size);
  bool (*retro_unserialize)(const void *data, size_t size);
  void (*retro_cheat_reset)(void);
  void (*retro_cheat_set)(unsigned index, bool enabled, const char *code);
  bool (*retro_load_game)(const struct retro_game_info* game);
  // bool (*retro_load_game_special)(
  //   unsigned game_type,
  //   const struct retro_game_info *info,
  //   size_t num_info);
  void (*retro_unload_game)(void);
  unsigned (*retro_get_region)(void);
  void * (*retro_get_memory_data)(unsigned id);
  size_t (*retro_get_memory_size)(unsigned id);

}
g_retro;

#define load_sym(V, S) do {\
  if (!((*(void**)&V) = dlsym(g_retro.handle, #S))) /** NOLINT **/ \
    die("[noarch] Failed to load symbol '" #S "'': %s", dlerror()); \
  } while (0)
#define load_retro_sym(S) load_sym(g_retro.S, S)

static void die(const char * fmt, ...) {
  char buffer[4096];

  va_list va;
  va_start(va, fmt);
  vsnprintf(buffer, sizeof(buffer), fmt, va);
  va_end(va);

  fputs(buffer, stderr);
  fputc('\n', stderr);
  fflush(stderr);

  exit(EXIT_FAILURE);
}

static void video_configure(const struct retro_game_geometry * geom) {
  width = geom->max_width;
  height = geom->max_height;
}

static void video_deinit() {}

static void audio_init(int frequency) {
  (void)frequency;
}

static void audio_deinit() {}

static void core_log(enum retro_log_level level, const char * fmt, ...) {
  char buffer[4096] = {0};
  static const char * levelstr[] = {
    "dbg",
    "inf",
    "wrn",
    "err"
  };
  va_list va;

  va_start(va, fmt);
  vsnprintf(buffer, sizeof(buffer), fmt, va);
  va_end(va);

  if (level == 0)
    return;

  fprintf(stderr, "[%s] %s", levelstr[level], buffer);
  fflush(stderr);

  if (level == RETRO_LOG_ERROR) {
    exit(EXIT_FAILURE);
  }
}

static bool core_environment(unsigned cmd, void * data) {
  switch (cmd) {
    case RETRO_ENVIRONMENT_GET_LOG_INTERFACE: {
      struct retro_log_callback* cb = (struct retro_log_callback*)data;
      cb->log = core_log;
    }
    break;

    case RETRO_ENVIRONMENT_GET_CAN_DUPE: {
      bool* bval = (bool*)data; // NOLINT
      *bval = true;
    }
    break;

    case RETRO_ENVIRONMENT_SET_PIXEL_FORMAT: {
      core_log(RETRO_LOG_DEBUG, "[noarch] RETRO_ENVIRONMENT_SET_PIXEL_FORMAT");
      return true;
    }

    case RETRO_ENVIRONMENT_GET_SYSTEM_DIRECTORY:
    case RETRO_ENVIRONMENT_GET_SAVE_DIRECTORY:
    case RETRO_ENVIRONMENT_GET_CONTENT_DIRECTORY:
    case RETRO_ENVIRONMENT_GET_LIBRETRO_PATH: {
      *(const char**)data = ".";
      return true;
    }

    case RETRO_ENVIRONMENT_SET_MESSAGE: {
      const struct retro_message* message = (const struct retro_message*)data;
      core_log(
        RETRO_LOG_DEBUG,
        "[noarch] RETRO_ENVIRONMENT_SET_MESSAGE: %s\n",
        message->msg);
      break;
    }

    case RETRO_ENVIRONMENT_SHUTDOWN: {
      core_log(RETRO_LOG_DEBUG, "[noarch] RETRO_ENVIRONMENT_SHUTDOWN");
      break;
    }

    default: {
      core_log(RETRO_LOG_DEBUG, "[noarch] Unhandled env #%u", cmd);
      return false;
    }
  }

  return true;
}

static void core_video_refresh(
      const void* data,
      unsigned width,
      unsigned height,
      size_t pitch) {
  (void)data;
  (void)width;
  (void)height;
  (void)pitch;

  if (data)
    g_retro.video_data = data;
  
  if (pitch) {
    g_retro.video_pitch = pitch;
  }
}

static void core_input_poll(void) {
  // Nothing
}

static int16_t core_input_state(
      unsigned port,
      unsigned device,
      unsigned index,
      unsigned id) {
  (void)port;
  (void)device;
  (void)index;
  (void)id;
  return 0;
}

static void core_audio_sample(int16_t left, int16_t right) {
  (void)left;
  (void)right;
}

static size_t core_audio_sample_batch(const int16_t * data, size_t frames) {
  (void)data;
  (void)frames;
  return 0;
}

static bool core_load(const char * sofile) {
  void (*set_environment)(retro_environment_t) = NULL;
  void (*set_video_refresh)(retro_video_refresh_t) = NULL;
  void (*set_input_poll)(retro_input_poll_t) = NULL;
  void (*set_input_state)(retro_input_state_t) = NULL;
  void (*set_audio_sample)(retro_audio_sample_t) = NULL;
  void (*set_audio_sample_batch)(retro_audio_sample_batch_t) = NULL;

  memset( (void *) & g_retro, 0, sizeof(g_retro));
  g_retro.handle = dlopen(sofile, RTLD_LAZY);

  if (!g_retro.handle) {
    printf("[noarch] Failed to load core: %s\n", dlerror());
    return false;
  }

  dlerror();

  load_retro_sym(retro_init);
  load_retro_sym(retro_deinit);
  load_retro_sym(retro_api_version);
  load_retro_sym(retro_get_system_info);
  load_retro_sym(retro_get_system_av_info);
  load_retro_sym(retro_set_controller_port_device);
  load_retro_sym(retro_reset);
  load_retro_sym(retro_run);
  load_retro_sym(retro_load_game);
  load_retro_sym(retro_unload_game);

  load_sym(set_environment, retro_set_environment);
  load_sym(set_video_refresh, retro_set_video_refresh);
  load_sym(set_input_poll, retro_set_input_poll);
  load_sym(set_input_state, retro_set_input_state);
  load_sym(set_audio_sample, retro_set_audio_sample);
  load_sym(set_audio_sample_batch, retro_set_audio_sample_batch);

  set_environment(core_environment);
  set_video_refresh(core_video_refresh);
  set_input_poll(core_input_poll);
  set_input_state(core_input_state);
  set_audio_sample(core_audio_sample);
  set_audio_sample_batch(core_audio_sample_batch);

  g_retro.retro_init();
  g_retro.initialized = true;

  return true;
}

static bool core_load_game(const char * filename) {
  struct retro_system_timing timing = {
    60.0f, 10000.0f
  };
  struct retro_game_geometry geom = {
    100, 100, 100, 100, 1.0f
  };
  struct retro_system_av_info av = {
    geom, timing
  };
  struct retro_system_info system = {
    0, 0, 0, false, false
  };

  struct retro_game_info info = {
    filename,
    0,
    0,
    NULL
  };

  FILE* file = NULL;
  if (filename) {
    file = fopen(filename, "rb");

    if (!file) {
      printf("[noarch] Error: Failed to load content from '%s'\n", filename);
      fclose(file);
      return false;
    }

    fseek(file, 0, SEEK_END);
    info.size = ftell(file);
    rewind(file);
  }

  g_retro.retro_get_system_info(&system);
  printf("[noarch] Info: %s %s\n", system.library_name, system.library_version);

  if (filename && !system.need_fullpath) {
    info.data = malloc(info.size);

    if (!info.data || !fread((void * ) info.data, info.size, 1, file)) { // NOLINT
      puts("[noarch] Error: Failed to load game data.");
      fclose(file);
      return false;
    }
    fclose(file);
  }

  if (!g_retro.retro_load_game(&info)) {
    puts("[noarch] The core failed to load the game.");
    return false;
  }

  g_retro.retro_get_system_av_info(&av);
  printf("[noarch] Video: %ix%i\n",
    av.geometry.base_width,
    av.geometry.base_height);

  video_configure(&av.geometry);
  audio_init(av.timing.sample_rate);
  return true;
}

static void core_unload() {
  if (g_retro.initialized) {
    g_retro.retro_deinit();
  }

  if (g_retro.handle) {
    dlclose(g_retro.handle);
  }
}

static void _retro_run(void) {
  if (g_retro.initialized)
    g_retro.retro_run();
}

static void _retro_reset(void) {
  if (g_retro.initialized)
    g_retro.retro_reset();
}

static bool _retro_load_game(const struct retro_game_info* game) {
  if (g_retro.initialized)
    return g_retro.retro_load_game(game);
  return false;
}

static void _retro_unload_game() {
  if (g_retro.initialized)
    g_retro.retro_unload_game();
}

static void _retro_get_memory_data(unsigned id) {
  if (g_retro.initialized)
    g_retro.retro_get_memory_data(id);
}

static size_t _retro_get_memory_size(unsigned id) {
  if (g_retro.initialized)
    return g_retro.retro_get_memory_size(id);
  return 0;
}


int main(int argc, char * argv[]) {
  // Ensure proper amount of arguments.
  if (argc < 2) {
    printf("Usage: %s <core> [game]\n", argv[0]);
    return 1;
  }

  // Load the core.
  if (!core_load(argv[1])) {
    return 1;
  }
  puts("[noarch] Core loaded");

  // Load the game if needed.
  if (!core_load_game((argc > 2) ? argv[2] : NULL)) {
    return 1;
  }

  // Run an iteration.
  puts("[noarch] retro_run()");
  g_retro.retro_run();

  // Unload the core.
  core_unload();
  audio_deinit();
  video_deinit();
  puts("[noarch] Core unloaded");

  return 0;
}


py::array_t<uint8_t> get_video_data() {
		long w = 100;
		long h = 100;

		py::array_t<uint8_t> arr({ { h, w, 3 } });
		uint8_t* data = arr.mutable_data();

    memmove(data, g_retro.video_data, h*w*3*sizeof(uint8_t));

		return arr;
}


PYBIND11_MODULE(libretro, m) {
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

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}