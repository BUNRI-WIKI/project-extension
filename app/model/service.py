from datetime import datetime

from app.model.schema import YoloModelResponse, KcbertModelResponse

def detect_recycle_image(model, image_url: str) -> YoloModelResponse:
    return YoloModelResponse( 
        responseTime= datetime.now(),
        result=model.get_yolo_result(image_url)
    )


def detect_hatespeech(model, sentence: str) -> KcbertModelResponse:
    return KcbertModelResponse(
        responseTime= datetime.now(),
        result=model.get_kcbert_result(sentence)
    )
