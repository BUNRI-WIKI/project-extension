from pydantic import BaseModel
from datetime import datetime

from typing import List, Optional

from enum import Enum


class ResourceType(str, Enum):
    url='url'
    btyes='bytes'

class YoloModelRequest(BaseModel):
    type: ResourceType
    resource: str

    class Config:  
        use_enum_values = True

class YoloModelResponse(BaseModel):
    responseTime: datetime
    result: Optional[List] = None


class KcbertModelRequest(BaseModel):
    resource: str

class KcbertModelResponse(BaseModel):
    responseTime: datetime
    result: Optional[List] = None
