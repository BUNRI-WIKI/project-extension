from ultralytics import YOLO
import json
from datetime import datetime

from app.model.constants import MODEL_PATH
from app.model.schema import ModelResponse

def model_detect(image_uri: str) -> ModelResponse:
    try:
        model = YOLO(MODEL_PATH)
        result = model(image_uri)[0]

    except Exception as e:
        print('YOLO Error')
        raise 
    
    return ModelResponse( 
        responseTime= datetime.now(),
        result= json.loads(result.tojson())
    )
