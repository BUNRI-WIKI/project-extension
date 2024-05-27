
from datetime import datetime

from app.yolo.model import YoloModel
from app.bert.model import KcBertModel
from app.model.schema import YoloModelResponse, KcbertModelResponse

def detect_recycle_image(lodder, image_uri: str) -> YoloModelResponse:
    model = YoloModel(lodder)
    return YoloModelResponse( 
        responseTime= datetime.now(),
        result=model.get_yolo_result(image_uri)
    )


def detect_hatespeech(lodder, sentence: str) -> KcbertModelResponse:
    model = KcBertModel(lodder)
    return KcbertModelResponse(
        responseTime= datetime.now(),
        result=model.get_kcbert_result(sentence)
    )
