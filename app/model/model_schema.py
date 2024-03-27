from pydantic import BaseModel

class ResultResponse(BaseModel):
    name: str
    confidence: float
    box: list[float]
