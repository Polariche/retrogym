from typing import TYPE_CHECKING, Any, List, Generic, SupportsFloat, TypeVar, Optional
import gymnasium as gym
from gymnasium import error,spaces
from gymnasium.error import DependencyNotInstalled
from gymnasium.utils import EzPickle
import numpy as np
import libretro 
import cv2
import utils

ObsType = TypeVar("ObsType")
ActType = TypeVar("ActType")
RenderFrame = TypeVar("RenderFrame")



class RetroEnv(gym.Env, EzPickle):
    metadata = {
        "render_modes": ["human", "rgb_array"]
    }

    def __init__(
        self,
        core: str,
        rom: str,
        ram: List[str] = [],
        state: Optional[str] = None,
        render_mode: Optional[str] = None,
    ):
        EzPickle.__init__(
            self,
            core,
            rom,
            render_mode,
        )

        self.emu = libretro.Emulator()
        self.emu.init(core)
        self.emu.load_game(rom)

        self.keys = self.emu.get_keys()
        self.ram = ram

        self.player_action = -1

        print(self.keys)
        if state is None:
            state = rom+".state"
        self.state = state

        self.action_space = spaces.Discrete(len(self.keys))
        self.observation_space = spaces.Box(0, 255, shape=(len(ram),), dtype=np.uint8)
        self.render_mode = render_mode

    def score(self, obs):
        return 0
    
    def done(self, obs):
        return False
    
    def step(self, action): #-> tuple[Any, SupportsFloat, bool, bool, dict[str, Any]]:
        for i, key in enumerate(self.keys):
            self.emu.set_key(key[0], action == i)

        self.emu.run()
        
        obs = [self.emu.get_memory_data(2, r - 0xC000) for r in self.ram]
        score = self.score(obs)
        done = self.done(obs)

        return obs, score, done, False, {}
    
    def reset(self, *, seed: Optional[int]= None, options: Optional[dict] = None, ): # -> tuple[ObsType, dict[str, Any]]:
        super().reset(seed=seed)
        obs, _, _, _, lab = self.step()

        return obs, lab

    def render(self, render_mode=None): #-> Optional[RenderFrame | list[RenderFrame]]:
        w = self.emu.width()
        h = self.emu.height()
        
        if not render_mode:
            render_mode = self.render_mode

        col = utils.group_argb565(self.emu.get_video()).astype(np.uint8).reshape(h,w,3)

        if render_mode == "rgb_array":
            return col
        
        elif render_mode == "human":
            cv2.imshow('', col[:,:,::-1])
            k = cv2.waitKey(6) & 0xFF
                        
            if k == 0xFF:
                self.player_action = -1
            elif k == 32:
                print("state saved: %s" % self.state)
                self.emu.save_state(self.state)
            else:
                try:
                    keymap = {122: 'A', 
                              120: 'B', 
                              82: 'Up', 
                              81: 'Left', 
                              83: 'Right', 
                              84: 'Down', 
                              13: 'Start', 
                              27: 'Select', 
                              97: 'L', 
                              100: 'R'}
                    action = {key[1]:i for i,key in enumerate(self.keys)}[keymap[k]]
                    
                    self.player_action = action

                    print(keymap[k], action)
                except:
                    print(k)

    
    def close(self):
        self.emu.deinit()