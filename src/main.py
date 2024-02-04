import libretro 
import numpy as np

import matplotlib.pyplot as plt
import random as rand

from env import *

import cv2 
import time

import argparse
import utils

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--core', '-c', dest='core', action="store", type=str,
                    help='Core file to load')
parser.add_argument('--rom', '-r', dest='rom', action="store", type=str,
                    help='ROM file to load')
parser.add_argument('--ram', dest='ram', action="append", type=str,
                    help='RAM to be used as observation for training')
parser.add_argument('--display', '-d', dest='display', action="store_true",
                    help='')
parser.add_argument('--loop', '-l', dest='loop', action="store", type=int, default=-1,
                    help='')
parser.add_argument('--delay', dest='delay', action="store", type=float, default=0.01,
                    help='')
parser.add_argument('--model', dest='model', action="store", type=str, default="random",
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


def model_loop(args, env, model=None):
    if args.model == "random":
        action = rand.choice(range(len(env.keys)))
    elif args.model == "human":
        action = env.player_action
    else: 
        action, _states = model.predict(obs)

    obs, rewards, dones, _, info = env.step(action)
    env.render()

    #print(','.join([str(o) for o in obs]))
    time.sleep(args.delay)


def main():
    args = parser.parse_args()
    args.ram = [int(r, 16) for r in args.ram]
    env = RetroEnv(core=args.core, 
                   rom=args.rom,
                   ram=args.ram,
                   render_mode="human")
    model = None
    loop = args.loop
    while loop != 0:
        model_loop(args, env, model)

        loop = max(-1, loop-1)


if __name__ == "__main__":
    main()

