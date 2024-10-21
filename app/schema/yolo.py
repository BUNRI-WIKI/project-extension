from pydantic import BaseModel, Field
from datetime import datetime

from typing import List, Optional

from enum import Enum

class ResourceType(str, Enum):
    url="url"
    btyes="bytes"

class YoloModelRequest(BaseModel):
    type: ResourceType = Field(example="url")
    resource: str = Field(example="https://trash-front-s3.s3.ap-northeast-2.amazonaws.com/images/KakaoTalk_20240606_145955920.png")

    class Config:  
        use_enum_values = True

class YoloModelResponse(BaseModel):
    responseTime: datetime = Field(example="2024-06-01T00:00:00.000000")
    result: Optional[List] = Field(
        example=[ 
                    {
                        "name": "pet",
                        "class": 3,
                        "confidence": 0.77605,
                        "box": {
                            "x1": 303.93634,
                            "y1": 343.60303,
                            "x2": 728.20624,
                            "y2": 1414.1405
                        }
                    }
                ]
    )
