from app.configs.logger import Logger

class ImageHandler:
    def check_image(self, image) -> bool:
        Logger.info('START IMAGE CHECK')
        if not self.check_image_size(image): return False

        Logger.success('IMAGE CHECK')
        return True
    
    def check_image_size(self, image) -> bool:
        Logger.info('START IMAGE SIZE CHECK')
        width, height, _ = image.shape()

        if (width if width < height else height) < 320:
            Logger.error('IMAGE SIZE EXCEPTION')
            return False
        
        Logger.success('IMAGE SIZE CHECK')
        return True
