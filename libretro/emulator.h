#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <stdbool.h>
#include <errno.h>
#include <dlfcn.h>

#include "libretro.h"

#define CALLBACK_SET_ENVIRONMENT        0
#define CALLBACK_SET_VIDEO_REFRESH      1
#define CALLBACK_SET_INPUT_POLL         2
#define CALLBACK_SET_INPUT_STATE        3
#define CALLBACK_SET_AUDIO_SAMPLE       4
#define CALLBACK_SET_AUDIO_SAMPLE_BATCH 5

class Core {
    private:
        void (*retro_set_environment)(retro_environment_t);
        void (*retro_set_video_refresh)(retro_video_refresh_t);
        void (*retro_set_input_poll)(retro_input_poll_t);
        void (*retro_set_input_state)(retro_input_state_t);
        void (*retro_set_audio_sample)(retro_audio_sample_t);
        void (*retro_set_audio_sample_batch)(retro_audio_sample_batch_t);

    public:
        void* handle = nullptr;

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
        void (*retro_unload_game)(void);
        unsigned (*retro_get_region)(void);
        void * (*retro_get_memory_data)(unsigned id);
        size_t (*retro_get_memory_size)(unsigned id);

        bool init(const char* core_path);
        void deinit();
        bool assign_callback(unsigned callback, void* func);
};

class Emulator {
    Core core;

    public:
        void* video_data = nullptr;

        bool core_load(const char* core_path);
        bool core_unload();
        bool game_load(const char* game_path);
        bool game_unload();
};