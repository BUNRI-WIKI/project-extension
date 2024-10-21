import cv2
import numpy as np
import requests

from app.configs.logger import Logger

IMG_FORMATS = {"jpeg", "jpg", "png"}

class Image:
    def __init__(self, request) -> None:
        self.__request = request.dict()
        self.__image = self.resourceToImage()

    def resource(self):
        return self.__request['resource']
    
    def get(self):
        return self.__image
    
    def shape(self):
        return self.__image.shape

    def resourceToImage(self):
        if self.__request['type'] == 'url': 
            Logger.info('IMAGE TYPE=URL')
            return self.urlToImage()
        
        else: 
            Logger.error('IMAGE TPYE EXCEPTION')
            return None

    def urlToImage(self):
        try:
            image_nparray = np.asarray(bytearray(requests.get(self.resource()).content), dtype=np.uint8)
            return cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
        
        except Exception as e:
            Logger.error('IMAGE READ EXCEPTION')
            raise
