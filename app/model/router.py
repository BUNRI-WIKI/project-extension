from fastapi import APIRouter, status, HTTPException

from app.image.util import Image
from app.image.handler import ImageHandler

from app.model import service
from app.model.schema import YoloModelResponse, YoloModelRequest, KcbertModelRequest, KcbertModelResponse

app = APIRouter(
    prefix="/models",
    tags=["models"],
)

handler = ImageHandler()

@app.get(path="/image-detection", 
         description="Recycled image detection & classification",
         response_model=YoloModelResponse,
         status_code=status.HTTP_200_OK)
async def model_detect(request: YoloModelRequest):
    image = Image(request)
    if not handler.check_image(image):
        raise HTTPException(status_code=404, detail="Item not found")
    return service.detect_recycle_image(image.get())


@app.get(path="/hatespeech-detection",
         description="Korean hate speech detection & classification",
         response_model=KcbertModelResponse,
         status_code=status.HTTP_200_OK)
async def model_hatespeech_detect(request: KcbertModelRequest):
    return service.detect_hatespeech(request.dict()['resource'])