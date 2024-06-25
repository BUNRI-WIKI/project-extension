from fastapi import FastAPI

from app.model import router

app = FastAPI(
    title="MIDAS",
    description="Object Detection and Object Classification API description for MIDAS",
    version="0.2.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(router.app)

@app.get("/")
def health_check():
    return {"health_check": "ok"}
