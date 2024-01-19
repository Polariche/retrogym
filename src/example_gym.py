import gymnasium as gym
from env import Retro2048Env

env = Retro2048Env(render_mode="human") #gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset(seed=42)

for _ in range(1000):
   action = env.action_space.sample()  # this is where you would insert your policy
   observation, reward, terminated, truncated, info = env.step(action)

   env.render()
   
   if terminated or truncated:
      observation, info = env.reset()

env.close()