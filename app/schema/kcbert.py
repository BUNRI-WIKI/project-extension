from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from app.utils.logger import Logger

class KcbertModelRequest(BaseModel):
    resource: str = Field(
        example="분리 수거를 위해선 본체에서 알루미늄 밑면을 칼로 말끔하게 도려낸 후, 뚜껑은 플라스틱, 밑면은 캔류로 분리 배출해요."
    )
    Logger.info("KcBERT model request initialized.")

class KcbertModelResponse(BaseModel):
    responseTime: datetime = Field(example="2024-06-01T00:00:00.000000")
    result: Optional[List[dict]] = Field(
        example=[
            {
                "일반문장": 97.14491367340088,
                "악플/욕설": 2.6516808196902275,
                "인종/국적": 0.06473279790952802,
                "성소수자": 0.03624645178206265,
                "여성/가족": 0.034627842251211405,
                "남성": 0.015888738562352955,
                "기타 혐오": 0.013659577234648168,
                "지역": 0.012289428559597582,
                "종교": 0.011726508819265291,
                "연령": 0.010931642464129254,
                "개인지칭": 0.003288640800747089
            }
        ]
    )
    Logger.info("KcBERT model response initialized.")
