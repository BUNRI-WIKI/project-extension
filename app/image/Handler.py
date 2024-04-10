class ImageHandler:
    def __init__(self,) -> None:
        pass

    def check_image(self, image) -> bool:
        print('start image_check')
        if not self.check_image_size(image): return False
        return True
    
    def check_image_size(self, image) -> bool:
        width, height, _ = image.shape()

        if (width if width < height else height) < 320:
            print('check_image_size Exception')
            return False
        
        return True
