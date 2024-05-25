
from datetime import datetime

from app.yolo.model import YoloModel
from app.bert.model import KcBertModel
from app.model.schema import YoloModelResponse, KcbertModelResponse

def detect_recycle_image(image_uri: str) -> YoloModelResponse:
    model = YoloModel()
    return YoloModelResponse( 
        responseTime= datetime.now(),
        result=model.get_yolo_result(image_uri)
    )


def detect_hatespeech(sentence: str) -> KcbertModelResponse:
    model = KcBertModel()
    return KcbertModelResponse(
        responseTime= datetime.now(),
        result=model.get_kcbert_result(sentence)
    )
