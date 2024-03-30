# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_emulator.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13grpc_emulator.proto\x12\x08retrogym\"\x19\n\tBoolValue\x12\x0c\n\x04\x62ool\x18\x01 \x01(\x08\"\x1b\n\nInt32Value\x12\r\n\x05int32\x18\x01 \x01(\x05\"\x1b\n\x0bPathRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"&\n\x03Key\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"+\n\x0cKeysResponse\x12\x1b\n\x04keys\x18\x01 \x03(\x0b\x32\r.retrogym.Key\"\x06\n\x04Void\"*\n\rSetKeyRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08\"\x1b\n\x0bImgResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x1f\n\x11MemorySizeRequest\x12\n\n\x02id\x18\x01 \x01(\r\"-\n\x11MemoryDataRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04\x61\x64\x64r\x18\x02 \x01(\r\"\"\n\x12MemorySizeResponse\x12\x0c\n\x04size\x18\x01 \x01(\r\"\"\n\x12MemoryDataResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\r2\xd6\x06\n\x0cGRPCEmulator\x12\x34\n\x04Init\x12\x15.retrogym.PathRequest\x1a\x13.retrogym.BoolValue\"\x00\x12/\n\x06\x44\x65init\x12\x0e.retrogym.Void\x1a\x13.retrogym.BoolValue\"\x00\x12\x38\n\x08LoadGame\x12\x15.retrogym.PathRequest\x1a\x13.retrogym.BoolValue\"\x00\x12\x33\n\nUnloadGame\x12\x0e.retrogym.Void\x1a\x13.retrogym.BoolValue\"\x00\x12\x39\n\tLoadState\x12\x15.retrogym.PathRequest\x1a\x13.retrogym.BoolValue\"\x00\x12\x39\n\tSaveState\x12\x15.retrogym.PathRequest\x1a\x13.retrogym.BoolValue\"\x00\x12,\n\x03Run\x12\x0e.retrogym.Void\x1a\x13.retrogym.BoolValue\"\x00\x12.\n\x05Reset\x12\x0e.retrogym.Void\x1a\x13.retrogym.BoolValue\"\x00\x12/\n\x05Width\x12\x0e.retrogym.Void\x1a\x14.retrogym.Int32Value\"\x00\x12\x30\n\x06Height\x12\x0e.retrogym.Void\x1a\x14.retrogym.Int32Value\"\x00\x12\x33\n\x07GetKeys\x12\x0e.retrogym.Void\x1a\x16.retrogym.KeysResponse\"\x00\x12\x33\n\x06SetKey\x12\x17.retrogym.SetKeyRequest\x1a\x0e.retrogym.Void\"\x00\x12\x33\n\x08GetVideo\x12\x0e.retrogym.Void\x1a\x15.retrogym.ImgResponse\"\x00\x12L\n\rGetMemorySize\x12\x1b.retrogym.MemorySizeRequest\x1a\x1c.retrogym.MemorySizeResponse\"\x00\x12L\n\rGetMemoryData\x12\x1b.retrogym.MemoryDataRequest\x1a\x1c.retrogym.MemoryDataResponse\"\x00\x42$\n\x0bio.retrogymB\rRetrogymProtoP\x01\xa2\x02\x03HLWb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_emulator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\013io.retrogymB\rRetrogymProtoP\001\242\002\003HLW'
  _globals['_BOOLVALUE']._serialized_start=33
  _globals['_BOOLVALUE']._serialized_end=58
  _globals['_INT32VALUE']._serialized_start=60
  _globals['_INT32VALUE']._serialized_end=87
  _globals['_PATHREQUEST']._serialized_start=89
  _globals['_PATHREQUEST']._serialized_end=116
  _globals['_KEY']._serialized_start=118
  _globals['_KEY']._serialized_end=156
  _globals['_KEYSRESPONSE']._serialized_start=158
  _globals['_KEYSRESPONSE']._serialized_end=201
  _globals['_VOID']._serialized_start=203
  _globals['_VOID']._serialized_end=209
  _globals['_SETKEYREQUEST']._serialized_start=211
  _globals['_SETKEYREQUEST']._serialized_end=253
  _globals['_IMGRESPONSE']._serialized_start=255
  _globals['_IMGRESPONSE']._serialized_end=282
  _globals['_MEMORYSIZEREQUEST']._serialized_start=284
  _globals['_MEMORYSIZEREQUEST']._serialized_end=315
  _globals['_MEMORYDATAREQUEST']._serialized_start=317
  _globals['_MEMORYDATAREQUEST']._serialized_end=362
  _globals['_MEMORYSIZERESPONSE']._serialized_start=364
  _globals['_MEMORYSIZERESPONSE']._serialized_end=398
  _globals['_MEMORYDATARESPONSE']._serialized_start=400
  _globals['_MEMORYDATARESPONSE']._serialized_end=434
  _globals['_GRPCEMULATOR']._serialized_start=437
  _globals['_GRPCEMULATOR']._serialized_end=1291
# @@protoc_insertion_point(module_scope)
