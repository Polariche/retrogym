# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_emulator_pb2 as grpc__emulator__pb2


class GRPCEmulatorStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Init = channel.unary_unary(
                '/retrogym.GRPCEmulator/Init',
                request_serializer=grpc__emulator__pb2.PathRequest.SerializeToString,
                response_deserializer=grpc__emulator__pb2.BoolValue.FromString,
                )
        self.Deinit = channel.unary_unary(
                '/retrogym.GRPCEmulator/Deinit',
                request_serializer=grpc__emulator__pb2.Void.SerializeToString,
                response_deserializer=grpc__emulator__pb2.BoolValue.FromString,
                )
        self.LoadGame = channel.unary_unary(
                '/retrogym.GRPCEmulator/LoadGame',
                request_serializer=grpc__emulator__pb2.PathRequest.SerializeToString,
                response_deserializer=grpc__emulator__pb2.BoolValue.FromString,
                )
        self.UnloadGame = channel.unary_unary(
                '/retrogym.GRPCEmulator/UnloadGame',
                request_serializer=grpc__emulator__pb2.Void.SerializeToString,
                response_deserializer=grpc__emulator__pb2.BoolValue.FromString,
                )
        self.LoadState = channel.unary_unary(
                '/retrogym.GRPCEmulator/LoadState',
                request_serializer=grpc__emulator__pb2.PathRequest.SerializeToString,
                response_deserializer=grpc__emulator__pb2.BoolValue.FromString,
                )
        self.SaveState = channel.unary_unary(
                '/retrogym.GRPCEmulator/SaveState',
                request_serializer=grpc__emulator__pb2.PathRequest.SerializeToString,
                response_deserializer=grpc__emulator__pb2.BoolValue.FromString,
                )
        self.Run = channel.unary_unary(
                '/retrogym.GRPCEmulator/Run',
                request_serializer=grpc__emulator__pb2.Void.SerializeToString,
                response_deserializer=grpc__emulator__pb2.BoolValue.FromString,
                )
        self.Reset = channel.unary_unary(
                '/retrogym.GRPCEmulator/Reset',
                request_serializer=grpc__emulator__pb2.Void.SerializeToString,
                response_deserializer=grpc__emulator__pb2.BoolValue.FromString,
                )
        self.Width = channel.unary_unary(
                '/retrogym.GRPCEmulator/Width',
                request_serializer=grpc__emulator__pb2.Void.SerializeToString,
                response_deserializer=grpc__emulator__pb2.Int32Value.FromString,
                )
        self.Height = channel.unary_unary(
                '/retrogym.GRPCEmulator/Height',
                request_serializer=grpc__emulator__pb2.Void.SerializeToString,
                response_deserializer=grpc__emulator__pb2.Int32Value.FromString,
                )
        self.GetKeys = channel.unary_unary(
                '/retrogym.GRPCEmulator/GetKeys',
                request_serializer=grpc__emulator__pb2.Void.SerializeToString,
                response_deserializer=grpc__emulator__pb2.KeysResponse.FromString,
                )
        self.SetKey = channel.unary_unary(
                '/retrogym.GRPCEmulator/SetKey',
                request_serializer=grpc__emulator__pb2.SetKeyRequest.SerializeToString,
                response_deserializer=grpc__emulator__pb2.Void.FromString,
                )
        self.GetMemorySize = channel.unary_unary(
                '/retrogym.GRPCEmulator/GetMemorySize',
                request_serializer=grpc__emulator__pb2.MemorySizeRequest.SerializeToString,
                response_deserializer=grpc__emulator__pb2.MemorySizeResponse.FromString,
                )
        self.GetMemoryData = channel.unary_unary(
                '/retrogym.GRPCEmulator/GetMemoryData',
                request_serializer=grpc__emulator__pb2.MemoryDataRequest.SerializeToString,
                response_deserializer=grpc__emulator__pb2.MemoryDataResponse.FromString,
                )


class GRPCEmulatorServicer(object):
    """The greeting service definition.
    """

    def Init(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deinit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnloadGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Run(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Width(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Height(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetKeys(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMemorySize(self, request, context):
        """rpc GetVideo
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMemoryData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GRPCEmulatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=grpc__emulator__pb2.PathRequest.FromString,
                    response_serializer=grpc__emulator__pb2.BoolValue.SerializeToString,
            ),
            'Deinit': grpc.unary_unary_rpc_method_handler(
                    servicer.Deinit,
                    request_deserializer=grpc__emulator__pb2.Void.FromString,
                    response_serializer=grpc__emulator__pb2.BoolValue.SerializeToString,
            ),
            'LoadGame': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadGame,
                    request_deserializer=grpc__emulator__pb2.PathRequest.FromString,
                    response_serializer=grpc__emulator__pb2.BoolValue.SerializeToString,
            ),
            'UnloadGame': grpc.unary_unary_rpc_method_handler(
                    servicer.UnloadGame,
                    request_deserializer=grpc__emulator__pb2.Void.FromString,
                    response_serializer=grpc__emulator__pb2.BoolValue.SerializeToString,
            ),
            'LoadState': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadState,
                    request_deserializer=grpc__emulator__pb2.PathRequest.FromString,
                    response_serializer=grpc__emulator__pb2.BoolValue.SerializeToString,
            ),
            'SaveState': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveState,
                    request_deserializer=grpc__emulator__pb2.PathRequest.FromString,
                    response_serializer=grpc__emulator__pb2.BoolValue.SerializeToString,
            ),
            'Run': grpc.unary_unary_rpc_method_handler(
                    servicer.Run,
                    request_deserializer=grpc__emulator__pb2.Void.FromString,
                    response_serializer=grpc__emulator__pb2.BoolValue.SerializeToString,
            ),
            'Reset': grpc.unary_unary_rpc_method_handler(
                    servicer.Reset,
                    request_deserializer=grpc__emulator__pb2.Void.FromString,
                    response_serializer=grpc__emulator__pb2.BoolValue.SerializeToString,
            ),
            'Width': grpc.unary_unary_rpc_method_handler(
                    servicer.Width,
                    request_deserializer=grpc__emulator__pb2.Void.FromString,
                    response_serializer=grpc__emulator__pb2.Int32Value.SerializeToString,
            ),
            'Height': grpc.unary_unary_rpc_method_handler(
                    servicer.Height,
                    request_deserializer=grpc__emulator__pb2.Void.FromString,
                    response_serializer=grpc__emulator__pb2.Int32Value.SerializeToString,
            ),
            'GetKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.GetKeys,
                    request_deserializer=grpc__emulator__pb2.Void.FromString,
                    response_serializer=grpc__emulator__pb2.KeysResponse.SerializeToString,
            ),
            'SetKey': grpc.unary_unary_rpc_method_handler(
                    servicer.SetKey,
                    request_deserializer=grpc__emulator__pb2.SetKeyRequest.FromString,
                    response_serializer=grpc__emulator__pb2.Void.SerializeToString,
            ),
            'GetMemorySize': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMemorySize,
                    request_deserializer=grpc__emulator__pb2.MemorySizeRequest.FromString,
                    response_serializer=grpc__emulator__pb2.MemorySizeResponse.SerializeToString,
            ),
            'GetMemoryData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMemoryData,
                    request_deserializer=grpc__emulator__pb2.MemoryDataRequest.FromString,
                    response_serializer=grpc__emulator__pb2.MemoryDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'retrogym.GRPCEmulator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GRPCEmulator(object):
    """The greeting service definition.
    """

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/Init',
            grpc__emulator__pb2.PathRequest.SerializeToString,
            grpc__emulator__pb2.BoolValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deinit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/Deinit',
            grpc__emulator__pb2.Void.SerializeToString,
            grpc__emulator__pb2.BoolValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/LoadGame',
            grpc__emulator__pb2.PathRequest.SerializeToString,
            grpc__emulator__pb2.BoolValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnloadGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/UnloadGame',
            grpc__emulator__pb2.Void.SerializeToString,
            grpc__emulator__pb2.BoolValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/LoadState',
            grpc__emulator__pb2.PathRequest.SerializeToString,
            grpc__emulator__pb2.BoolValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/SaveState',
            grpc__emulator__pb2.PathRequest.SerializeToString,
            grpc__emulator__pb2.BoolValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Run(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/Run',
            grpc__emulator__pb2.Void.SerializeToString,
            grpc__emulator__pb2.BoolValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/Reset',
            grpc__emulator__pb2.Void.SerializeToString,
            grpc__emulator__pb2.BoolValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Width(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/Width',
            grpc__emulator__pb2.Void.SerializeToString,
            grpc__emulator__pb2.Int32Value.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Height(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/Height',
            grpc__emulator__pb2.Void.SerializeToString,
            grpc__emulator__pb2.Int32Value.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetKeys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/GetKeys',
            grpc__emulator__pb2.Void.SerializeToString,
            grpc__emulator__pb2.KeysResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/SetKey',
            grpc__emulator__pb2.SetKeyRequest.SerializeToString,
            grpc__emulator__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMemorySize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/GetMemorySize',
            grpc__emulator__pb2.MemorySizeRequest.SerializeToString,
            grpc__emulator__pb2.MemorySizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMemoryData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/retrogym.GRPCEmulator/GetMemoryData',
            grpc__emulator__pb2.MemoryDataRequest.SerializeToString,
            grpc__emulator__pb2.MemoryDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
