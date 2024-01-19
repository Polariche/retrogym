from typing import TYPE_CHECKING, Any, Generic, SupportsFloat, TypeVar, Optional
import gymnasium as gym
from gymnasium import error,spaces
from gymnasium.error import DependencyNotInstalled
from gymnasium.utils import EzPickle
import numpy as np
import libretro 

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
        self.observation_space = spaces.Box(0, np.inf, shape=(4,4))
    
    def _boot(self):
        self.emu = libretro.Emulator()
        self.emu.init("cores/2048/2048_libretro.so")

    def step(self, action: ActType) -> tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]:
        self.emu.set_key(1 << action)
        self.emu.run()
        data = self.emu.get_memory_data(0)
        score = data[0]
        obs = data[]
    
    def reset(self, *, seed: Optional[int]= None, options: Optional[dict] = None, ) -> tuple[ObsType, dict[str, Any]]:
        self.emu.reset()

    def render(self) -> Optional[RenderFrame | list[RenderFrame]]:
        frame = group_argb8888(self.emu.get_video())
        return frame
    
    def close(self):
        self.emu.deinit()