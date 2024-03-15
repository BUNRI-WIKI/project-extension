from fastapi import APIRouter

from model import model_service

app = APIRouter(
    prefix="/models",
)

@app.get(path="/detect/{image_url:path}", description="Image Detection & Image Classification")
async def image_detect(image_url: str):
    return model_service.image_detect(image_url)