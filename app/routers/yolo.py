from fastapi import APIRouter, status, Depends

from app.crud import yolo
from app.schema.yolo import YoloModelResponse, YoloModelRequest
from app.models.yolo_model import YoloModel
from app.utils.image import Image
from app.utils.logger import Logger
from app.main import get_yolo_model

router = APIRouter(
    prefix="/yolo",
    tags=["yolo"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    path="/prediction", 
    description="Recycled image detection & classification",
    response_model=YoloModelResponse,
    status_code=status.HTTP_200_OK
)
async def predict_yolo(
    request: YoloModelRequest,
    model: YoloModel = Depends(get_yolo_model)
):
    """
    Predict the classification of a given image using YOLO model.
    
    Parameters:
    request (YoloModelRequest): The request containing image information (URL or Base64).
    model (YoloModel): The YOLO model instance used for prediction (injected by FastAPI's dependency system).

    Returns:
    YoloModelResponse: The classification result as a response model.
    """
    Logger.info(f"Received prediction request for image resource: {request.resource}")

    try:
        # Create an Image instance and pass it to the YOLO model for detection
        image = Image(request)
        result = yolo.detect_recycle_image(model, image)
        Logger.info("YOLO prediction successful.")
    except Exception as e:
        Logger.error(f"Error occurred during YOLO prediction: {str(e)}")
        raise e

    return result
