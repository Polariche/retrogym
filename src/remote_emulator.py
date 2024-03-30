import grpc
import grpc_emulator_pb2
import grpc_emulator_pb2_grpc

import numpy as np
import struct

class RemoteEmulator():

    def __init__(self, path):
        self.channel = grpc.insecure_channel(path)
        self.stub = grpc_emulator_pb2_grpc.GRPCEmulatorStub(self.channel)

    def __del__(self):
        print("closing")

        self.unload_game()
        self.deinit()
        self.channel.close()
        

    def init(self, core_path):
        return self.stub.Init(grpc_emulator_pb2.PathRequest(path=core_path)).bool

    def deinit(self):
        return self.stub.Deinit(grpc_emulator_pb2.Void()).bool

    def width(self):
        return self.stub.Width(grpc_emulator_pb2.Void()).int32

    def height(self):
        return self.stub.Height(grpc_emulator_pb2.Void()).int32

    def load_game(self, game_path):
        return self.stub.LoadGame(grpc_emulator_pb2.PathRequest(path=game_path)).bool

    def unload_game(self):
        return self.stub.UnloadGame(grpc_emulator_pb2.Void()).bool

    def load_state(self, state_path):
        return self.stub.LoadState(grpc_emulator_pb2.PathRequest(path=state_path)).bool

    def save_state(self, state_path):
        return self.stub.SaveState(grpc_emulator_pb2.PathRequest(path=state_path)).bool

    def run(self):
        return self.stub.Run(grpc_emulator_pb2.Void()).bool
    
    def reset(self):
        return self.stub.Reset(grpc_emulator_pb2.Void())

    def get_keys(self):
        res = []

        for k in self.stub.GetKeys(grpc_emulator_pb2.Void()).keys:
            res.append((k.id, k.description))
            
        return res

    def set_key(self, id, value):
        self.stub.SetKey(grpc_emulator_pb2.SetKeyRequest(id=id, value=value))

    def get_video(self):
        raw = self.stub.GetVideo(grpc_emulator_pb2.Void()).data
        
        return np.array([d for d in struct.iter_unpack('H', raw)], dtype=np.uint16) # # #
    
    def get_memory_size(self, id):
        return self.stub.GetMemorySize(grpc_emulator_pb2.MemorySizeRequest(id=id)).size

    def get_memory_data(self, id, addr):
        return self.stub.GetMemoryData(grpc_emulator_pb2.MemoryDataRequest(id=id, addr=addr)).data