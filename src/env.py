from typing import TYPE_CHECKING, Any, Generic, SupportsFloat, TypeVar, Optional
import gymnasium as gym
from gymnasium import error,spaces
from gymnasium.error import DependencyNotInstalled
from gymnasium.utils import EzPickle
import nympy as np


ObsType = TypeVar("ObsType")
ActType = TypeVar("ActType")
RenderFrame = TypeVar("RenderFrame")

class RetroEnv(gym.Env, EzPickle):

    def __init__(
        self,
        render_mode: Optional[str] = None,
        rom_path,
        obs_ram_map,
    ):
        EzPickle.__init__(
            self,
            render_mode,
        )

        self.action_space = spaces.Box(-1, +1, (2,), dtype=np.float32)
        self.observation_space = spaces.Box(np.array([-1]), np.array([1]))
    
    def _boot(self):
        raise NotImplementedError

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