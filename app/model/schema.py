from pydantic import BaseModel
from datetime import datetime

from typing import List, Optional

from enum import Enum

class ResourceType(str, Enum):
    url='url'
    btyes='bytes'


class ModelRequest(BaseModel):
    type: ResourceType
    resource: str

    class Config:  
        use_enum_values = True


class ModelResponse(BaseModel):
    responseTime: datetime
    result: Optional[List] = None
