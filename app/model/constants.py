import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "yolo.pt")


class NoResultsOfModelException(Exception):

    def __init__(self):
        super.__init__("There are no results for this model")

    