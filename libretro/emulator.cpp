#include "emulator.h"

bool Core::init(const char* core_path) {
    if (!(handle = dlopen(core_path, RTLD_LAZY)))
        return false;

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

    (*(void**)&retro_set_environment) = dlsym(handle, "retro_set_environment");
    (*(void**)&retro_set_video_refresh) = dlsym(handle, "retro_set_video_refresh");
    (*(void**)&retro_set_input_poll) = dlsym(handle, "retro_set_input_poll");
    (*(void**)&retro_set_input_state) = dlsym(handle, "retro_set_input_state");
    (*(void**)&retro_set_audio_sample) = dlsym(handle, "retro_set_audio_sample");
    (*(void**)&retro_set_audio_sample_batch) = dlsym(handle, "retro_set_audio_sample_batch");

    return true;
}

void Core::deinit() {
    if (handle != nullptr)
        dlclose(handle);
    handle = nullptr;
}

bool Core::assign_callback(unsigned callback, void* func) {
    switch(callback) {
        case CALLBACK_SET_ENVIRONMENT:
            retro_set_environment((retro_environment_t)func); break;
        case CALLBACK_SET_VIDEO_REFRESH:
            retro_set_video_refresh((retro_video_refresh_t)func); break;
        case CALLBACK_SET_INPUT_POLL:
            retro_set_input_poll((retro_input_poll_t)func); break;
        case CALLBACK_SET_INPUT_STATE:
            retro_set_input_state((retro_input_state_t)func); break;
        case CALLBACK_SET_AUDIO_SAMPLE:
            retro_set_audio_sample((retro_audio_sample_t)func); break;
        case CALLBACK_SET_AUDIO_SAMPLE_BATCH:
            retro_set_audio_sample_batch((retro_audio_sample_batch_t)func); break;
    }
}

bool Emulator::core_load(const char* core_path) {
    if (!(core.init(core_path))) {
        // TODO put error msg
        return false;
    }
    core.retro_init();
}

bool Emulator::core_unload() {
    core.deinit();
    core.retro_deinit();
}

bool Emulator::game_load(const char* game_path) {

}

bool Emulator::game_unload() {
    
}
