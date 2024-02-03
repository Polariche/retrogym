from typing import TYPE_CHECKING, Any, Generic, SupportsFloat, TypeVar, Optional
import gymnasium as gym
from gymnasium import error,spaces
from gymnasium.error import DependencyNotInstalled
from gymnasium.utils import EzPickle
import numpy as np
import libretro 
import cv2

ObsType = TypeVar("ObsType")
ActType = TypeVar("ActType")
RenderFrame = TypeVar("RenderFrame")

def group_argb8888(data):
    return np.array(data).reshape(-1,4)[:,:3]

class Retro2048Env(gym.Env, EzPickle):
    metadata = {
        "render_modes": ["human", "rgb_array"]
    }

    def __init__(
        self,
        render_mode: Optional[str] = None,
    ):
        EzPickle.__init__(
            self,
            render_mode,
        )

        self._boot()
        obs_size = 16 #int(self.emu.get_memory_size(0)/4)-10

        print(self.emu.get_keys())

        self.action_space = spaces.Discrete(4) 
        self.observation_space = spaces.Box(0, 17, shape=(obs_size,), dtype=int)
        self.render_mode = render_mode

    
    def _boot(self):
        self.emu = libretro.Emulator()
        self.emu.init("cores/2048_libretro.so")
        self.emu.load_game("roms/pokemon_red.gb")
            
    def _start_game(self):
        self.emu.reset()
        data = self.emu.get_memory_data_b4(0)

        if (data[2] == 0 or data[2] == 2):
            for i, _ in self.emu.get_keys():
                self.emu.set_key(i, False)
            self.emu.set_key(3, True)
            self.emu.run()
            data = self.emu.get_memory_data_b4(0)

        return data[10::10]
    

    def step(self, action): #-> tuple[Any, SupportsFloat, bool, bool, dict[str, Any]]:
        for i, _ in self.emu.get_keys():
            self.emu.set_key(i, False)
        self.emu.set_key(action+4, True)
        self.emu.run()
        
        data = self.emu.get_memory_data_b4(0)
        obs = data[10::10]
        done = data[2] == 2

        score = (np.log2(data[0]) if data[0] > 0 else 0)
        
        return obs, score, done, False, {}
    
    def reset(self, *, seed: Optional[int]= None, options: Optional[dict] = None, ): # -> tuple[ObsType, dict[str, Any]]:
        super().reset(seed=seed)

        data = self._start_game()
        return data, {}

    def render(self, render_mode=None): #-> Optional[RenderFrame | list[RenderFrame]]:
        w = self.emu.width()
        h = self.emu.height()
        
        if not render_mode:
            render_mode = self.render_mode
        col = group_argb8888(self.emu.get_video()).reshape(h,w,3)

        if render_mode == "rgb_array":
            col = np.concatenate([col[:,:,2:],col[:,:,1:2],col[:,:,:1]], axis=2)
            return col
        
        elif render_mode == "human":
            cv2.imshow('', col.reshape(h,w,3))
            cv2.waitKey(1)
    
    def close(self):
        self.emu.deinit()