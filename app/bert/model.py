import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from app.configs.lodder import Lodder
from app.configs.logger import Logger

class KcBertModel:
    def __init__(self) -> None:
        self.__model_name = 'beomi/kcbert-base'

        self.model = AutoModelForSequenceClassification.from_pretrained(self.__model_name, num_labels=11)
        self.tokenizer = AutoTokenizer.from_pretrained(self.__model_name)
        Logger.success('KcBERT MODEL INIT')

    def get_kcbert_result(self, setence: str) -> list:
        Logger.info('START KcBERT MODEL LOAD')
        try:
            self.model.load_state_dict(Lodder.load_kcbert_model())
            self.model.eval()

            encoding = self.tokenizer(setence, padding=True, truncation=True, return_tensors="pt")

            with torch.no_grad():
                result = self.model(**encoding).logits[0]
        
        except Exception as e:
            Logger.error('KcBERT MODEL LOAD EXCEPTION')
            raise 
        
        Logger.success('KcBERT MODEL LOAD')
        result = [{self.__change_label(idx) : result[idx].item() for idx in torch.argsort(result, descending=True)}]
        return result
    
    def __change_label(self, label) -> str:
        if label == 0:      return '여성/가족'
        elif label == 1:    return '남성'
        elif label == 2:    return '성소수자'
        elif label == 3:    return '인종/국적'
        elif label == 4:    return '연령'
        elif label == 5:    return '지역'
        elif label == 6:    return '종교'
        elif label == 7:    return '기타 혐오'
        elif label == 8:    return '악플/욕설'
        elif label == 9:    return '개인지칭'
        else:               return '일반문장'