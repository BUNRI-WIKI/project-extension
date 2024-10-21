from fastapi import APIRouter, status, HTTPException

from app.configs.lodder import Lodder
from app.image.util import Image
from app.image.handler import ImageHandler
from app.model import service
from app.model.schema import YoloModelResponse, YoloModelRequest, KcbertModelRequest, KcbertModelResponse

app = APIRouter(
    prefix="/models",
    tags=["models"],
)

handler = ImageHandler()
lodder = Lodder()

from app.yolo.model import YoloModel
from app.bert.model import KcBertModel
yolo_model = YoloModel(lodder)
kcbert_model = KcBertModel(lodder)

@app.get(path="/image-detection", 
         description="Recycled image detection & classification",
         response_model=YoloModelResponse,
         status_code=status.HTTP_200_OK)
async def image_detect_and_classification(request: YoloModelRequest):
    image = Image(request)
    if not handler.check_image(image):
        raise HTTPException(status_code=404, detail="Item not found")
    return service.detect_recycle_image(yolo_model, image.get())


@app.get(path="/hatespeech-detection",
         description="Korean hate speech detection & classification",
         response_model=KcbertModelResponse,
         status_code=status.HTTP_200_OK)
async def hatespeech_detect_and_classification(request: KcbertModelRequest):
    return service.detect_hatespeech(kcbert_model, request.dict()['resource'])