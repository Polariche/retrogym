# Installation
Install dependencies
```
sudo apt-get update
sudo apt-get install -y python3-dev build-essential libgl1-mesa-glx libglib2.0-0 
sudo apt-get install -y '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev libsm6 libxext6 libxrender-dev
```

(Optional) Build GRPC Emulator
```
mkdir -p cmake/build
cd cmake/build
cmake ../../
make
```

Create & activate venv
```
python3 -m venv venv
. venv/bin/activate
```

Install requirements & RetroGym
```
pip install -r requirements.txt
python setup.py install
```

# Config
You can customize an experiment by writing a config file. Refer to `data` folder for example config.

* `core` is the emulator library for Libretro to use when loading a ROM.

* `rom` is the game ROM we use for experiments.

* `state` is the game state to load when the game resets.

* `actions` is the list of inputs allowed throughout the experiment.

* `observations` is the list of variables we feed into the reinforcement model. The values are parsed directly from RAM according to `address`; to extract the values you need you need to refer to [a RAM map](https://datacrystal.romhacking.net/wiki/Pok%C3%A9mon_Red_and_Blue/RAM_map).

* `rewards` reads variables from `observations`, and evaluates rewards based on them. Currently available values for `condition` are `new`, `duplicate`, `changed`, `unchangd`, and `default`.

* `endings` determines when to reset the environment based on `observations`. Currently available available values for `condition` are `match` and `timeout`.


# Usage

To randomize the inputs, run the following command:
```
python src/main.py --config data/rival_battle.yaml --model random
```



To train a PPO model (implemented by Stable Baselines3), run:
```
python src/main.py --config data/rival_battle.yaml --model PPO --model-file models/rival --train
```

You may test the trained model by removing `--train` 

```
python src/main.py --config data/rival_battle.yaml --model PPO --model-file models/rival
```
You should see something along the GIF below:

![gif](https://raw.githubusercontent.com/Polariche/retrogym/main/docs/rival_example.gif)

# References

This project has gotten so far thanks to:


https://github.com/libretro/RetroArch

https://github.com/libretro/libretro-2048

https://github.com/Farama-Foundation/Gymnasium

https://github.com/openai/retro

https://github.com/DLR-RM/stable-baselines3

https://github.com/PWhiddy/PokemonRedExperiments