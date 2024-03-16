import libretro 
import numpy as np

import matplotlib.pyplot as plt
import random as rand

from env import *

import cv2 
import time

import argparse
import utils

from gymnasium.wrappers import TransformObservation
from stable_baselines3.common.vec_env import DummyVecEnv


parser = argparse.ArgumentParser(description='Process some integers.')


parser.add_argument('--config', dest='config', action="store", type=str,
                    help='config file location')
parser.add_argument('--model-file', dest='model_file', action="store", type=str,
                    help='model location')
parser.add_argument('--loop', '-l', dest='loop', action="store", type=int, default=100000,
                    help='')
parser.add_argument('--model', dest='model', action="store", type=str, default="random",
                    help='')
parser.add_argument('--train', dest='train', action="store_true",
                    help='')

def random_loop(args, e):
    # loop without Gymnasium env

    keys =  e.get_keys()
    w,h = e.width(), e.height()

    for i, _ in keys:
        e.set_key(i, False)
    cur_key = rand.choice(keys)
    e.set_key(cur_key[0], True)

    e.run()
    time.sleep(args.delay)

    if args.ram is not None:
        print(','.join([str(e.get_memory_data(2, r - 0xC000)) for r in args.ram]))

    if args.display:
        video_data = e.get_video()
        col = utils.group_argb565(video_data).reshape(h,w,3).astype(np.uint8)
        col = col[:,:,::-1]     # rgb -> bgr swap for cv2
        cv2.imshow('', col)
        cv2.waitKey(1)


def model_loop(args, env, model, obs):
    if args.model == "random":
        action = np.array([env.action_space.sample()])
    elif args.model == "human":
        action = np.array([env.envs[0].player_action])
    else: 
        action, _states = model.predict(obs)

    obs, rewards, dones, info = env.step(action)
    env.render()

    return obs

from stable_baselines3 import PPO, DQN
models = {"PPO": PPO, "DQN": DQN}

def make_model(name, env):
    if name in ["PPO", "DQN"]:
        return models[name]("MultiInputPolicy", env, verbose=1)
    else:
        return None

def load_model(name, filename):
    try:
        return models[name].load(filename)
    except:
        return None

def main():
    args = parser.parse_args()
    config = utils.read_config_from_yaml(args.config)

    env = RetroEnv(config=config,
                   render_mode="human")
    
    env = DummyVecEnv([lambda: env])
    
    loop = args.loop

    if args.train:
        model = make_model(args.model, env)
        model.learn(total_timesteps=loop, progress_bar=True)
        model.save(args.model_file)
    else:
        model = load_model(args.model, args.model_file)
        cnt = 0
        obs = env.reset()
        while loop != 0:
            obs = model_loop(args, env, model, obs)
            
            loop = max(-1, loop-1)
            cnt += 1


if __name__ == "__main__":
    main()

