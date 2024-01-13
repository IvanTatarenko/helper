from src.services.folder.folder_service import FolderService
from src.services.logger.logger_service import LoggerService
from PIL import Image



class ResizeImageService:
  def __init__(self):
    self.logger = LoggerService(ResizeImageService.__name__)
    self.folder_service = FolderService()

  def height_800(self) -> Image:
    """Зміна розміру картинки по висоті на 800px зі збереженням пропорцій """
    self.logger.info('Запуск сервісу зміни розміру картинок')
    self.folder_service.create_base_folders()
    self.logger.success('Виконано')

    