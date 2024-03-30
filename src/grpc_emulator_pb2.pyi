from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BoolValue(_message.Message):
    __slots__ = ("bool",)
    BOOL_FIELD_NUMBER: _ClassVar[int]
    bool: bool
    def __init__(self, bool: bool = ...) -> None: ...

class Int32Value(_message.Message):
    __slots__ = ("int32",)
    INT32_FIELD_NUMBER: _ClassVar[int]
    int32: int
    def __init__(self, int32: _Optional[int] = ...) -> None: ...

class PathRequest(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class Key(_message.Message):
    __slots__ = ("id", "description")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: int
    description: str
    def __init__(self, id: _Optional[int] = ..., description: _Optional[str] = ...) -> None: ...

class KeysResponse(_message.Message):
    __slots__ = ("keys",)
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[Key]
    def __init__(self, keys: _Optional[_Iterable[_Union[Key, _Mapping]]] = ...) -> None: ...

class Void(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetKeyRequest(_message.Message):
    __slots__ = ("id", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    value: bool
    def __init__(self, id: _Optional[int] = ..., value: bool = ...) -> None: ...

class ImgResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class MemorySizeRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class MemoryDataRequest(_message.Message):
    __slots__ = ("id", "addr")
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDR_FIELD_NUMBER: _ClassVar[int]
    id: int
    addr: int
    def __init__(self, id: _Optional[int] = ..., addr: _Optional[int] = ...) -> None: ...

class MemorySizeResponse(_message.Message):
    __slots__ = ("size",)
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: int
    def __init__(self, size: _Optional[int] = ...) -> None: ...

class MemoryDataResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int
    def __init__(self, data: _Optional[int] = ...) -> None: ...
