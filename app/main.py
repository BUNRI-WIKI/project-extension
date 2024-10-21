from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.utils.logger import Logger


kcbert_model_instance = None
yolo_model_instance = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    from app.routers import yolo, kcbert
    from app.models.loader import S3ModelLoader
    from app.models.kcbert_model import KcBertModel
    from app.models.yolo_model import YoloModel

    global kcbert_model_instance, yolo_model_instance

    Logger.info("start server")
    s3_loader = S3ModelLoader()

    kcbert_model, kcbert_tokenizer = s3_loader.load_kcbert_model()
    yolo_model = s3_loader.load_yolo_model()
    
    kcbert_model_instance = KcBertModel(kcbert_model, kcbert_tokenizer)
    yolo_model_instance = YoloModel(yolo_model)
    
    app.include_router(yolo.router)
    app.include_router(kcbert.router)
    Logger.info("Finish Init")
    
    yield
    
    Logger.info("close server")


def get_kcbert_model():
    return kcbert_model_instance

def get_yolo_model():
    return yolo_model_instance


app = FastAPI(
    title="MIDAS",
    description="Object Detection and Object Classification API description for MIDAS",
    version="0.3.0",
    lifespan=lifespan,
)

@app.get("/")
def health_check():
    return {"Health Check": "OK"}
