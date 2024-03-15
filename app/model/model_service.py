from ultralytics import YOLO

from model.constants import NoResultsOfModelException, MODEL_PATH

def image_detect(image_url: str):
    yolo_model = YOLO(MODEL_PATH)

    try:    
        result = yolo_model(image_url)[0]

        if result is None:
            raise NoResultsOfModelException

    except NoResultsOfModelException as e:
        print(e)
        return {}
    
    print(result)

    return {
        'boxes' : result.boxes,
        'probs' : result.probs
        }
    