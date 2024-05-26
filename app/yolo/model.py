import json

from ultralytics import YOLO
from app.configs.lodder import Lodder
from app.configs.logger import Logger

class YoloModel:
    def __init__(self) -> None:

        self.__lodder = Lodder()


    def get_yolo_result(self, image_uri):
        Logger.info('START YOLO MODEL LOAD')
        try:
            model = self.__lodder.load_yolo_model('yolo.pt')
            result = model(image_uri)[0]

        except Exception as e:
            Logger.error('YOLO MODEL LOAD EXCEPTION')
            raise 

        Logger.success('KcBERT MODEL LOAD')
        return json.loads(result.tojson())
