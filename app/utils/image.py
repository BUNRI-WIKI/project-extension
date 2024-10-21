from app.utils.logger import Logger

class Image:
    IMG_FORMATS = {"jpeg", "jpg", "png"}

    def __init__(self, request):
        """
        Initialize the Image object.
        
        Parameters:
        request (dict): The request data containing image resource information. 
                        The resource could be a URL or base64-encoded image data.
        """
        request = request.dict()

        self.resource = request["resource"]
        self.image = self.urlToImage() if request["type"] == "url" else None
        Logger.info(f"Image initialized with resource: {self.resource}")

    def get(self):
        """
        Get the image data after conversion.
        
        Returns:
        image (np.ndarray): The processed image data.
        """
        Logger.info("Fetching the processed image data.")
        return self.image

    def urlToImage(self):
        """
        Convert an image from URL to an OpenCV-compatible format.
        
        This method fetches the image from the provided URL and converts it to a NumPy array.

        Returns:
        np.ndarray: The image data in OpenCV format.
        
        Raises:
        Exception: If the image cannot be fetched or processed.
        """
        import cv2
        import numpy as np
        import requests

        Logger.info(f"Fetching image from URL: {self.resource}")

        try:
            # Fetching image data from the URL
            image_nparray = np.asarray(bytearray(requests.get(self.resource).content), dtype=np.uint8)
            Logger.info("Image fetched successfully from URL.")
            
            # Decoding the image data to OpenCV format
            return cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)
        except Exception as e:
            Logger.error(f"Error occurred while fetching or decoding the image: {str(e)}")
            raise e
