from typing import Any, List

from fastapi import APIRouter, status
from model.model_schema import ResultResponse

from model import model_service

app = APIRouter(
    prefix="/models",
)

@app.get(path="/detect/{image_url:path}", 
         description="Image Detection & Image Classification",
         response_model=List[ResultResponse],
         status_code=status.HTTP_200_OK)
async def image_detect(image_url: str) -> Any:
    return model_service.image_detect(image_url)