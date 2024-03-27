from ultralytics import YOLO
import pandas as pd
import numpy as np

from app.model.model_schema import ResultResponse
from app.model.constants import NoResultsOfModelException, MODEL_PATH

'''
for test dataset 
https://img.danawa.com/cms/img/images/000393/20171115051433496_HNZHKQ12.jpg

'''
def getReuslt(result):
    boxes = result.boxes.numpy()
    categories = result.names

    values = {
        'class': boxes.cls,
        'confidence': boxes.conf,
        'box': boxes.xyxy.tolist()
    }

    df = pd.DataFrame(values)
    
    df['name'] = df['class'].apply(lambda x: categories[x])

    df = df[['name', 'confidence', 'box']]

    sorted_df = df.sort_values(by='confidence', ascending=False)

    result_dict = sorted_df.to_dict(orient='records')

    return result_dict


def image_detect(image_uri: str):
    model = YOLO(MODEL_PATH)

    try:
        result = model(image_uri)[0]

        if result is None:
            raise NoResultsOfModelException

    except NoResultsOfModelException as e:
        print(e)
        
        return {}
    
    return getReuslt(result)
    