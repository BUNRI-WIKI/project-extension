import cv2
import numpy as np
import requests

IMG_FORMATS = {"jpeg", "jpg", "png"}

class Image:
    def __init__(self, rsrc) -> None:
        self.__rsrc = rsrc.dict()
        self.__image = self.ResourceToImage()

    def resource(self):
        return self.__rsrc['resource']
    
    def get(self):
        return self.__image
    
    def shape(self):
        return self.__image.shape

    def ResourceToImage(self,):
        if self.__rsrc['type'] == 'url': return self.UrlToImage()
        else: return None

    def UrlToImage(self):
        try:
            image_nparray = np.asarray(bytearray(requests.get(self.resource()).content), dtype=np.uint8)
            return cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
        
        except Exception as e:
            print('url_image_read Exception')
            raise
