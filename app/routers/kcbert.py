from fastapi import APIRouter, status, Depends

from app.crud import kcbert
from app.schema.kcbert import KcbertModelRequest, KcbertModelResponse
from app.models.kcbert_model import KcBertModel
from app.utils.logger import Logger
from app.main import get_kcbert_model

router = APIRouter(
    prefix="/kcbert",
    tags=["kcbert"],
    responses={404: {"description": "Not found"}},
)

@router.get(
    path="/prediction",
    description="Korean hate speech detection & classification",
    response_model=KcbertModelResponse,
    status_code=status.HTTP_200_OK,
)
async def predict(
    request: KcbertModelRequest, 
    model: KcBertModel = Depends(get_kcbert_model)
):
    """
    Predict the sentiment or hate speech classification of a given text.

    Parameters:
    request (KcbertModelRequest): The request body containing the text to be classified.
    model (KcBertModel): The KcBERT model instance used for prediction (injected by FastAPI's dependency system).

    Returns:
    KcbertModelResponse: The classification result as a response model.
    """
    Logger.info(f"Received prediction request for text: {request.resource}")

    try:
        # Call the detection function and log the result
        result = kcbert.detect_hatespeech(model, request.dict()["resource"])
        Logger.info(f"Prediction successful for text: {request.resource}")
    except Exception as e:
        Logger.error(f"Error occurred during prediction: {str(e)}")
        raise e

    return result
