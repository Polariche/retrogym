import numpy as np
from pydantic import BaseModel, validator
from pydantic_yaml import parse_yaml_raw_as, to_yaml_str
from models import ConfigModel, ObservationModel, RewardModel, EndingModel

def group_argb565(data):
    data = np.array(data).reshape(-1)
    
    r = (data & 0xF800) >> 8
    g = (data & 0x07E0) >> 3
    b = (data & 0x001F) << 3

    return np.stack([r,g,b], axis=1)

def parse_ram(emu, addr):
    if ":" in addr:
        s, e = addr.split(":")
        s = int(s, 16)
        e = int(e, 16)

        return [emu.get_memory_data(2, addr - 0xC000) for addr in range(s,e+1)]
    else:
        addr = int(addr, 16)
        return [emu.get_memory_data(2, addr - 0xC000)]
    

def parse_ram_size(addr):
    if ":" in addr:
        s, e = addr.split(":")
        s = int(s, 16)
        e = int(e, 16)

        return e-s+1
    else:
        return 1
    

def read_config_from_yaml(config):
    with open(config, "r") as f:
        m = parse_yaml_raw_as(ConfigModel, ''.join(f.readlines()))
    return m