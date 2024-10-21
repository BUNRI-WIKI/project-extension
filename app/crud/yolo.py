from datetime import datetime

from app.schema.yolo import YoloModelResponse
from app.models.yolo_model import YoloModel
from app.utils.image import Image
from app.utils.logger import Logger

def detect_recycle_image(model: YoloModel, image: Image) -> YoloModelResponse:
    """
    Detect and classify recyclable materials in the given image using the YOLO model.
    
    Parameters:
    model (YoloModel): The YOLO model used to perform the prediction.
    image (Image): The image object containing the input image data (e.g., URL or base64).

    Returns:
    YoloModelResponse: The response containing the classification results and response time.
    """
    Logger.info(f"Starting image classification for resource: {image.resource}")

    try:
        # Call the YOLO model's prediction function
        result = model.predict(image)
        Logger.info("Image classification successful.")
    except Exception as e:
        Logger.error(f"Error during image classification: {str(e)}")
        raise e

    # Return the prediction result wrapped in a YoloModelResponse object
    return YoloModelResponse(
        responseTime=datetime.now(),
        result=result
    )
