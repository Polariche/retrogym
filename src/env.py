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
    def __init__(
        self,
        render_mode: Optional[str] = None,
    ):
        EzPickle.__init__(
            self,
            render_mode,
        )

        self._boot()

        self.action_space = spaces.Discrete(4) 
        self.observation_space = spaces.Box(0, np.inf, shape=(self.emu.get_memory_size(0)))
        self.render_mode = render_mode
    
    def _boot(self):
        self.emu = libretro.Emulator()
        self.emu.init("cores/2048/2048_libretro.so")
        self._start_game()
            
    def _start_game(self):
        data = self.emu.get_memory_data(0)

        if (data[2] == 0):
            self.emu.set_key(1 << 3)
            self.emu.run()

    def step(self, action: ActType) -> tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]:
        self.emu.set_key(1 << (action+4))
        self.emu.run()
        data = self.emu.get_memory_data(0)

        score = data[0]
        obs = data
        done = data[2] == 2

        return obs, score, done, False, {}
    
    def reset(self, *, seed: Optional[int]= None, options: Optional[dict] = None, ) -> tuple[ObsType, dict[str, Any]]:
        self.emu.reset()
        self._start_game()

    def render(self) -> Optional[RenderFrame | list[RenderFrame]]:
        col = group_argb8888(self.emu.get_video()).reshape(464,376,3)

        if self.render_mode == "rgb_array":
            col = col.swapaxes(0,1) 
            frame = np.concatenate([col[:,:,2:],col[:,:,1:2],col[:,:,:1]])
            return frame
        
        elif self.render_mode == "human":
            cv2.imshow('', col.reshape(464,376,3))
            cv2.waitKey(1)
    
    def close(self):
        self.emu.deinit()