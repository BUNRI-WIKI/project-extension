from app.utils.logger import Logger
from app.utils.image import Image

class YoloModel:
    def __init__(self, model=None):
        """
        Initialize the YOLO model.
        
        Parameters:
        model: The pre-trained YOLO model instance to be used for predictions.
        """
        self.model = model
        Logger.info("YOLO model initialized.")

    def predict(self, image: Image):
        """
        Make a prediction using the YOLO model.
        
        Parameters:
        image (Image): The image object to be processed and predicted by the YOLO model.
        
        Returns:
        dict: A dictionary containing the model's predictions in JSON format.
        """
        import json

        Logger.info(f"Starting prediction for image resource: {image.resource}")
        
        try:
            # Perform the prediction on the input image
            result = self.model(image.get())[0]
            Logger.info("Prediction successful.")
        except Exception as e:
            Logger.error(f"Error during YOLO prediction: {str(e)}")
            raise e

        # Return the prediction results as a JSON object
        return json.loads(result.to_json())
