import numpy as np

def group_argb565(data):
    data = np.array(data).reshape(-1)
    
    r = (data & 0xF800) >> 8
    g = (data & 0x07E0) >> 3
    b = (data & 0x001F) << 3

    return np.stack([r,g,b], axis=1)