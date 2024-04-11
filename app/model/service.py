from ultralytics import YOLO
import json
from datetime import datetime

from app.configs.logger import Logger
from app.model.constants import MODEL_PATH
from app.model.schema import ModelResponse

def model_detect(image_uri: str) -> ModelResponse:
    try:
        model = YOLO(MODEL_PATH)
        result = model(image_uri)[0]

    except Exception as e:
        Logger.error('YOLO MODEL EXCEPTION')
        raise 
    
    return ModelResponse( 
        responseTime= datetime.now(),
        result= json.loads(result.tojson())
    )
