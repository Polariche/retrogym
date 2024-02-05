#include "emulator.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <stdbool.h>
#include <errno.h>
#include <dlfcn.h>

static Emulator * _e;

void Emulator::default_log_cb(enum retro_log_level level, const char * fmt, ...) {
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

bool Emulator::default_env_cb(unsigned cmd, void * data) {
  switch (cmd) {
    case RETRO_ENVIRONMENT_SET_INPUT_DESCRIPTORS: {
      retro_input_descriptor* a = reinterpret_cast<retro_input_descriptor*>(data);
      for(int i=0; a[i].device; i++) {
        _e->input_desc.push_back(a[i]);
      }
    }
    break;
    case RETRO_ENVIRONMENT_GET_LOG_INTERFACE: {
      struct retro_log_callback* cb = (struct retro_log_callback*)data;
      cb->log = default_log_cb;
    }
    break;

    case RETRO_ENVIRONMENT_GET_CAN_DUPE: {
      bool* bval = (bool*)data; // NOLINT
      *bval = true;
    }
    break;

    case RETRO_ENVIRONMENT_SET_PIXEL_FORMAT: {
      _e->pixel_format = *reinterpret_cast<unsigned*> (data);
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
      default_log_cb(
        RETRO_LOG_DEBUG,
        "[gym] RETRO_ENVIRONMENT_SET_MESSAGE: %s\n",
        message->msg);
      break;
    }

    case RETRO_ENVIRONMENT_SHUTDOWN: {
      default_log_cb(RETRO_LOG_DEBUG, "[gym] RETRO_ENVIRONMENT_SHUTDOWN");
      break;
    }

    default: {
      default_log_cb(RETRO_LOG_DEBUG, "[gym] Unhandled env #%u", cmd);
      return false;
    }
  }

  return true;
}

void Emulator::default_video_cb(
      const void* data,
      unsigned width,
      unsigned height,
      size_t pitch) {
    _e->video_data = data;
    _e->video_pitch = pitch;
}
void Emulator::default_input_poll_cb(void) {
}
int16_t Emulator::default_input_state_cb(
      unsigned port,
      unsigned device,
      unsigned index,
      unsigned id) {
  return _e->input[id];
}

void Emulator::default_audio_cb(int16_t left, int16_t right) {
}
size_t Emulator::default_audio_b_cb(const int16_t * data, size_t frames) {
  return 0;
}

bool Core::init(const char* core_path) {
    if (!(handle = dlopen(core_path, RTLD_LAZY)))
        return false;
    
    dlerror();

    (*(void**)&retro_init) = dlsym(handle, "retro_init");
    (*(void**)&retro_deinit) = dlsym(handle, "retro_deinit");
    (*(void**)&retro_api_version) = dlsym(handle, "retro_api_version");
    (*(void**)&retro_get_system_info) = dlsym(handle, "retro_get_system_info");
    (*(void**)&retro_get_system_av_info) = dlsym(handle, "retro_get_system_av_info");
    (*(void**)&retro_set_controller_port_device) = dlsym(handle, "retro_set_controller_port_device");
    (*(void**)&retro_reset) = dlsym(handle, "retro_reset");
    (*(void**)&retro_run) = dlsym(handle, "retro_run");
    (*(void**)&retro_load_game) = dlsym(handle, "retro_load_game");
    (*(void**)&retro_unload_game) = dlsym(handle, "retro_unload_game");
    (*(void**)&retro_get_region) = dlsym(handle, "retro_get_region");
    (*(void**)&retro_get_memory_size) = dlsym(handle, "retro_get_memory_size");
    (*(void**)&retro_get_memory_data) = dlsym(handle, "retro_get_memory_data");
    (*(void**)&retro_serialize_size) = dlsym(handle, "retro_serialize_size");
    (*(void**)&retro_serialize) = dlsym(handle, "retro_serialize");
    (*(void**)&retro_unserialize) = dlsym(handle, "retro_unserialize");

    (*(void**)&retro_set_environment) = dlsym(handle, "retro_set_environment");
    (*(void**)&retro_set_video_refresh) = dlsym(handle, "retro_set_video_refresh");
    (*(void**)&retro_set_input_poll) = dlsym(handle, "retro_set_input_poll");
    (*(void**)&retro_set_input_state) = dlsym(handle, "retro_set_input_state");
    (*(void**)&retro_set_audio_sample) = dlsym(handle, "retro_set_audio_sample");
    (*(void**)&retro_set_audio_sample_batch) = dlsym(handle, "retro_set_audio_sample_batch");

    retro_set_environment(env_cb);
    retro_set_video_refresh(video_cb);
    retro_set_input_poll(input_poll_cb);
    retro_set_input_state(input_state_cb);
    retro_set_audio_sample(audio_cb);
    retro_set_audio_sample_batch(audio_b_cb);

    retro_init();
    
    return true;
}

void Core::deinit() {
    retro_deinit();

    if (handle != nullptr)
        dlclose(handle);
    handle = nullptr;
}

bool Core::assign_callback(unsigned callback, void* func) {
    switch(callback) {
        case CALLBACK_SET_ENVIRONMENT:
            env_cb = (retro_environment_t)func; break;
        case CALLBACK_SET_VIDEO_REFRESH:
            video_cb = (retro_video_refresh_t)func; break;
        case CALLBACK_SET_INPUT_POLL:
            input_poll_cb = (retro_input_poll_t)func; break;
        case CALLBACK_SET_INPUT_STATE:
            input_state_cb = (retro_input_state_t)func; break;
        case CALLBACK_SET_AUDIO_SAMPLE:
            audio_cb = (retro_audio_sample_t)func; break;
        case CALLBACK_SET_AUDIO_SAMPLE_BATCH:
            audio_b_cb = (retro_audio_sample_batch_t)func; break;
        default:
            return false;
    }
    return true;
}

bool Emulator::core_load(const char* core_path) {
    _e = this;

    core.assign_callback(CALLBACK_SET_ENVIRONMENT, (void*) default_env_cb);
    core.assign_callback(CALLBACK_SET_VIDEO_REFRESH, (void*) default_video_cb);
    core.assign_callback(CALLBACK_SET_INPUT_POLL, (void*) default_input_poll_cb);
    core.assign_callback(CALLBACK_SET_INPUT_STATE, (void*) default_input_state_cb);
    core.assign_callback(CALLBACK_SET_AUDIO_SAMPLE, (void*) default_audio_cb);
    core.assign_callback(CALLBACK_SET_AUDIO_SAMPLE_BATCH, (void*) default_audio_b_cb);

    if (!(core.init(core_path))) {
        // TODO put error msg
        return false;
    }
    return true;
}

bool Emulator::core_unload() {
    core.deinit();
    return true;
}

bool Emulator::game_load(const char* game_path) {
    struct retro_system_info system = {
      0, 0, 0, false, false
    };
    struct retro_game_info info = {game_path, 0, 0, NULL};
    struct retro_system_av_info av = {
      {100, 100, 100, 100, 1.0f}, // geometry
      {60.0f, 10000.0f}           // timing
    };
    
    core.retro_get_system_info(&system);

    FILE * file=NULL;
    if (game_path) {
      
      file = fopen(game_path, "rb");

      if (!file) {
        fclose(file);
        return false;
      }
        
      fseek(file, 0, SEEK_END);
      info.size = ftell(file);
      
      rewind(file);

      if (!system.need_fullpath) {
        info.data = malloc(info.size);

        if (!info.data || !fread((void * ) info.data, info.size, 1, file)) { // NOLINT
          fclose(file);
          return false;
        }
        fclose(file);
      }
    }

    if (!core.retro_load_game(&info))
      return false;

    core.retro_get_system_av_info(&av);

    // get width and height
    width = av.geometry.base_width;
    height = av.geometry.base_height;

    return true;
}

bool Emulator::game_unload() {
    core.retro_unload_game();
    return false;
}

bool Emulator::state_load(const char* state_path) {
    size_t size = core.retro_serialize_size();
    FILE * file=NULL;
    void* data = malloc(size);
    bool success = false;

    if (state_path) {
      file = fopen(state_path, "rb");

      if (!file) {
        fclose(file);
        return false;
      }

      if ((success = fread((void * ) data, size, 1, file))) {
        success &= core.retro_unserialize(data, size);
      }
      fclose(file);
    }

    free(data);
    return success;
}


bool Emulator::state_save(const char* state_path) {
    
    size_t size = core.retro_serialize_size();
    FILE * file=NULL;

    void* data = malloc(size);
    bool success = false;

    if (state_path) {
      file = fopen(state_path, "wb");
      
      if (!file) {
        fclose(file);
        return false;
      }

      core.retro_serialize(data, size);
      success = fwrite((void * ) data, size, 1, file);
      fclose(file);
    }

    free(data);
    return success;
}
