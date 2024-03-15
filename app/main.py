from fastapi import FastAPI

from model import model_router

app = FastAPI()

app.include_router(model_router.app, tags=["model"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

