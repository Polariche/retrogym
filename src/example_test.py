import gymnasium as gym
from env import Retro2048Env
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3 import PPO


def make_env():
    env = Retro2048Env(render_mode="human") #gym.make(config["env_name"], render_mode="rgb_array")
    return env


# Create and wrap the environment
env = make_env()
env = DummyVecEnv([lambda: env])

# model = A2C("MlpPolicy", env, ent_coef=0.1, verbose=1)
# # Train the agent
# model.learn(total_timesteps=100000, progress_bar=True)
# # Save the agent
# model.save("a2c_lunar")
# del model  # delete trained model to demonstrate loading

# Load the trained agent
model = PPO.load("models/u1t4v1e7/model")

# Enjoy trained agent
obs = env.reset()
for i in range(10000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()