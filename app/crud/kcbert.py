from datetime import datetime

from app.schema.kcbert import KcbertModelResponse
from app.models.kcbert_model import KcBertModel
from app.utils.logger import Logger

def detect_hatespeech(model: KcBertModel, sentence: str) -> KcbertModelResponse:
    """
    Detect and classify hate speech in the given sentence using the KcBERT model.
    
    Parameters:
    model (KcBertModel): The KcBERT model used to perform the prediction.
    sentence (str): The sentence to classify, detecting possible hate speech.

    Returns:
    KcbertModelResponse: The response containing the classification results and response time.
    """
    Logger.info(f"Starting hate speech detection for sentence: {sentence}")
    
    try:
        # Call the KcBERT model's prediction function
        result = model.predict(sentence)
        Logger.info("Hate speech detection successful.")
    except Exception as e:
        Logger.error(f"Error during hate speech detection: {str(e)}")
        raise e

    # Return the prediction result wrapped in a KcbertModelResponse object
    return KcbertModelResponse(
        responseTime=datetime.now(),
        result=result
    )
