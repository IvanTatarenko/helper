import os
from PIL import Image, IOError
from services.logger.logger_service import LoggerService

class ImageService:
  def __init__(self):
    self.logger = LoggerService(ImageService.__name__)

  def __resize_height_image(self, image: Image, new_height: int) -> Image:
    """Зміна розміру картинки по висоті зі збереженням пропорцій"""
    try:
      width, height = image.size
      new_width = int(new_height * width / height)
      resize_image = image.resize((new_width, new_height), Image.ANTIALIAS)
      self.logger.success(f'Розмір зображення змінено на {new_height}px х {new_width}px')
      return resize_image
    except Exception as err:
      self.logger.err('Помилка під час зміни розміру зображення:')
      self.logger.err(err)



  def __open_image(self, path: str) -> Image:
    """Відкриваємо зображення за шляхом"""
    try:
      image = Image.open(path)
      self.logger.success(f'Отримали зображення за шляхом - {path}')
      return image
    except IOError as err:
      self.logger.err(f'Помилка під час відкриття зображення:')
      self.logger.err(err)
    except Exception as err:
      self.logger.err(f'Несподівана помилка під час відкриття зображення:')
      self.logger.err(err)

  def __save_Image(self, image: Image, save_path: str):
    try:
      image.save(save_path)
      self.logger.success(f'Зображення збережено за шляхом - {save_path}')
    except IOError as err:
      self.logger.err(f'Помилка під час збереження зображення:')
      self.logger.err(err)
    except Exception as err:
      self.logger.err(f'Несподівана помилка під час збереження зображення:')
      self.logger.err(err)
    