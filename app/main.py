from fastapi import FastAPI

from app.model import model_router

app = FastAPI(
    title="MIDAS",
    description="Object Detection and Object Classification API description for MIDAS",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(model_router.app, tags=["model"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

