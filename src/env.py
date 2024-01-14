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
        libretro.core_load("cores/2048/2048_libretro.so")

    def step(self, action: ActType) -> tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]:
        libretro.retro_run()
    
    def reset(self, *, seed: Optional[int]= None, options: Optional[dict] = None, ) -> tuple[ObsType, dict[str, Any]]:
        libretro.retro_reset()

    def render(self) -> Optional[RenderFrame | list[RenderFrame]]:
        raise NotImplementedError
    
    def close(self):
        libretro.core_unload()


class ChromiumEnv(gym.Env):
    def __init__(
        self,
        render_mode: Optional[str] = None,
    ):
        EzPickle.__init__(
            self,
            render_mode,
        )

        self.action_space = spaces.Box(-1, +1, (2,), dtype=np.float32)
        self.observation_space = spaces.Box(np.array([-1]), np.array([1]))
    
    def step(self, action: ActType) -> tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]:
        raise NotImplementedError
    
    def reset(self, *, seed: Optional[int]= None, options: Optional[dict] = None, ) -> tuple[ObsType, dict[str, Any]]:
        raise NotImplementedError

    def render(self) -> Optional[RenderFrame | list[RenderFrame]]:
        raise NotImplementedError
    
    def close(self):
        pass


class HTTPEnv(gym.Env):
    def __init__(
        self,
        render_mode: Optional[str] = None,
    ):
        EzPickle.__init__(
            self,
            render_mode,
        )

        self.action_space = spaces.Box(-1, +1, (2,), dtype=np.float32)
        self.observation_space = spaces.Box(np.array([-1]), np.array([1]))
    
    def step(self, action: ActType) -> tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]:
        raise NotImplementedError
    
    def reset(self, *, seed: Optional[int]= None, options: Optional[dict] = None, ) -> tuple[ObsType, dict[str, Any]]:
        raise NotImplementedError

    def render(self) -> Optional[RenderFrame | list[RenderFrame]]:
        raise NotImplementedError
    
    def close(self):
        pass


