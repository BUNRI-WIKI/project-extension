from app.utils.logger import Logger

class KcBertModel:
    def __init__(self, model=None, tokenizer=None):
        """
        Initialize KcBERT Model and Tokenizer.
        
        Parameters:
        model: The pre-trained KcBERT model instance.
        tokenizer: The tokenizer associated with the KcBERT model.
        """
        self.model = model
        self.tokenizer = tokenizer
        Logger.info("KcBertModel initialized with model and tokenizer.")

    def predict(self, sentence: str) -> list:
        """
        Make a prediction using the KcBERT model.
        
        Parameters:
        sentence (str): The input sentence to be classified.
        
        Returns:
        list: A list containing the classification result as a dictionary 
        where the key is the label and the value is the percentage confidence.
        """
        import torch
        import torch.nn.functional as F

        Logger.info(f"Predicting label for sentence: {sentence}")
        
        try:
            # Tokenize the input sentence
            encoding = self.tokenizer(sentence, padding=True, truncation=True, return_tensors="pt")
            Logger.info("Sentence tokenized successfully.")

            # Perform the prediction without calculating gradients
            with torch.no_grad():
                logit = self.model(**encoding).logits[0]
                result = F.softmax(F.log_softmax(logit, dim=0), dim=0)
                Logger.info("Model prediction computed successfully.")
        
        except Exception as e:
            Logger.error(f"Error occurred during prediction: {str(e)}")
            raise e
        
        # Returning the label with the percentage confidence
        return [{self._change_label(idx): result[idx].item() * 100 for idx in torch.argsort(result, descending=True)}]
    
    def _change_label(self, label) -> str:
        """
        Map numerical label to human-readable string.
        
        Parameters:
        label (int): The predicted label index.
        
        Returns:
        str: The corresponding human-readable label.
        """
        label_map = {
            0: "여성/가족",
            1: "남성",
            2: "성소수자",
            3: "인종/국적",
            4: "연령",
            5: "지역",
            6: "종교",
            7: "기타 혐오",
            8: "악플/욕설",
            9: "개인지칭",
            10: "일반문장"
        }
        return label_map.get(label, "Unknown")
