from pydantic import BaseModel
from typing import ForwardRef
from typing import List, Optional, Union


class ObservationModel(BaseModel):
    name: str
    space: str
    address: Optional[str] = ''


RewardModel = ForwardRef('RewardModel')
class RewardModel(BaseModel):
    type: str
    targets: Optional[List[str]] = []
    reward: Optional[float] = 0

RewardModel.update_forward_refs()


class EndingModel(BaseModel):
    type: str
    targets: Optional[List[str]] = []
    values: Optional[List[Union[str, int, float]]] = []


class ConfigModel(BaseModel):
    core: str
    rom: str
    state: str
    actions: List[str]
    observations: List[ObservationModel]
    rewards: List[RewardModel]
    endings: List[EndingModel]