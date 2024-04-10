from fastapi import APIRouter, status, HTTPException

from app.image.util import Image
from app.image.Handler import ImageHandler

from app.model import service
from app.model.schema import ModelResponse, ModelRequest

app = APIRouter(
    prefix="/models",
    tags=["models"],
)

Handler = ImageHandler()

@app.get(path="/detection", 
         description="Image Detection & Image Classification",
         response_model=ModelResponse,
         status_code=status.HTTP_200_OK)
async def model_detect(image_resource: ModelRequest):
    image = Image(image_resource)
    print('clear Image init')
    if not Handler.check_image(image):
        raise HTTPException(status_code=404, detail="Item not found")
    print('clear image_check')
    return service.model_detect(image.get())