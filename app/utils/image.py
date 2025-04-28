import cv2
import numpy as np
import requests
import base64

from app.utils.logger import Logger
from app.schema.yolo import YoloModelRequest

class Image:
    IMG_FORMATS = {"jpeg", "jpg", "png"}

    def __init__(self, request: YoloModelRequest):
        """
        Initialize the Image object based on the input request.
        """
        request_data = request.dict()

        self.resource = request_data["resource"]
        self.type = request_data["type"]

        if self.type == "url":
            self.image = self._url_to_image(self.resource)
        elif self.type == "bytes":
            self.image = self._base64_to_image(self.resource)
        else:
            Logger.error(f"Unsupported image type: {self.type}")
            raise ValueError(f"Unsupported image type: {self.type}")

        Logger.info(f"Image initialized with type {self.type} and resource {self.resource}")

    def get(self) -> np.ndarray:
        """
        Get the decoded image data.
        """
        Logger.info("Fetching the processed image data.")
        return self.image

    @staticmethod
    def _url_to_image(url: str) -> np.ndarray:
        """
        Fetch an image from a URL and convert it to OpenCV format.
        """
        Logger.info(f"Fetching image from URL: {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
            image_nparray = np.frombuffer(response.content, dtype=np.uint8)
            image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
            if image is None:
                raise ValueError("Failed to decode image")
            Logger.info("Image fetched and decoded successfully from URL.")
            return image
        except Exception as e:
            Logger.error(f"Error during URL to image conversion: {str(e)}")
            raise

    @staticmethod
    def _base64_to_image(b64_string: str) -> np.ndarray:
        """
        Convert a base64-encoded string to OpenCV format.
        """
        Logger.info("Converting base64 string to image.")
        try:
            img_data = base64.b64decode(b64_string)
            np_arr = np.frombuffer(img_data, np.uint8)
            image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            if image is None:
                raise ValueError("Failed to decode base64 image")
            Logger.info("Base64 image decoded successfully.")
            return image
        except Exception as e:
            Logger.error(f"Error during base64 to image conversion: {str(e)}")
            raise