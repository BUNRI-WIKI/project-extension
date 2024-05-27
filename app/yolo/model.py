import json

from app.configs.logger import Logger

class YoloModel:
    def __init__(self, lodder) -> None:
        self.__lodder = lodder


    def get_yolo_result(self, image_uri):
        Logger.info('START YOLO MODEL LOAD')
        try:
            model = self.__lodder.get_yolo_model()
            result = model(image_uri)[0]

        except Exception as e:
            Logger.error('YOLO MODEL LOAD EXCEPTION')
            raise 

        Logger.success('KcBERT MODEL LOAD')
        return json.loads(result.tojson())
