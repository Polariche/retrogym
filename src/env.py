from typing import TYPE_CHECKING, Any, List, Generic, SupportsFloat, TypeVar, Optional
import gymnasium as gym
from gymnasium import error,spaces
from gymnasium.error import DependencyNotInstalled
from gymnasium.utils import EzPickle
import numpy as np
import libretro 
import cv2
import utils
import rewards
import endings
import os 
from models import ConfigModel
from remote_emulator import RemoteEmulator

ObsType = TypeVar("ObsType")
ActType = TypeVar("ActType")
RenderFrame = TypeVar("RenderFrame")



class RetroEnv(gym.Env, EzPickle):
    metadata = {
        "render_modes": ["human", "rgb_array"]
    }

    def __init__(
        self,
        config: ConfigModel,
        render_mode: Optional[str] = None,
        remote: Optional[str] = None,
    ):
        EzPickle.__init__(
            self,
            config.core,
            config.rom,
            config.state,
            config.actions,
            render_mode,
        )

        remote = "0.0.0.0:50001"
        if remote is not None:
            self.emu = RemoteEmulator(remote)
        else: 
            self.emu = libretro.Emulator()
            
        self.emu.init(config.core)
        self.emu.load_game(config.rom)
        self.config = config
        self.state = config.state

        self.keys = self.emu.get_keys()
        if config.actions is not None:
            self.keys = [k for k in self.keys if k[1] in config.actions]     # use only directional keys

        self.player_action = -1

        self.action_space = spaces.Discrete(len(self.keys))
        self.observation_space = spaces.Dict(
                                    {obs.name:spaces.Box(0, 255, shape=(utils.parse_ram_size(obs.address),)) for obs in self.config.observations}
                                )
        self.render_mode = render_mode

    def obs(self):
        return {obs.name:utils.parse_ram(self.emu, obs.address) for obs in self.config.observations}
        
    def get_reward(self, past_obs, action, obs):
        for r in self.rewards:
            res = r.get_reward(past_obs, action, obs)
            if res > 0 or res < 0:
                return res
    
    def done(self, past_obs, action, obs):
        for e in self.endings:
            if e.done(past_obs, action, obs):
                return True
        return False
    
    def step(self, action): #-> tuple[Any, SupportsFloat, bool, bool, dict[str, Any]]:
        past_obs = self.obs()

        for i, key in enumerate(self.keys):
            self.emu.set_key(key[0], action == i)

        for _ in range(12):
            self.emu.run()

        obs = self.obs()
        
        reward = self.get_reward(past_obs, action, obs)
        done = self.done(past_obs, action, obs)

        return obs, reward, done, False, {}
    
    def reset(self, *, seed: Optional[int]= None, options: Optional[dict] = None, ): # -> tuple[ObsType, dict[str, Any]]:
        super().reset(seed=seed)

        self.rewards = [rewards.create_reward(r) for r in self.config.rewards]
        self.endings = [endings.create_ending(e) for e in self.config.endings]

        if os.path.isfile(self.state): 
            self.emu.load_state(self.state)
        else:
            print(f"'{self.state}' doesn't exist; skip loading")
        obs, _, _, _, lab = self.step(-1)

        print("reset!")

        return obs, lab
    

    def human_control(self, k):
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
            except:
                pass


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
            k = cv2.waitKey(1) & 0xFF
            self.human_control(k)
    
    def close(self):
        self.emu.deinit()
                        
    