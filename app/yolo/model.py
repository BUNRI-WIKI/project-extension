import json

from ultralytics import YOLO
from app.configs.lodder import Lodder

class YoloModel:
    def __init__(self) -> None:
        self.__model = YOLO()

    def get_yolo_result(self, image_uri):
        result = self.__model(image_uri)[0]
        return json.loads(result.tojson())
