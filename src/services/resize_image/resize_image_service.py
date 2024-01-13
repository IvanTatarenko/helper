from src.services.folder.folder_service import FolderService
from src.services.logger.logger_service import LoggerService
from PIL import Image
from typing import List
import os



class ResizeImageService:
  def __init__(self):
    self.logger = LoggerService(ResizeImageService.__name__)
    self.folder_service = FolderService()
    self.IMPORT_PATH = os.path.abspath('import')

  def height_800(self) -> Image:
    """Зміна розміру картинки по висоті на 800px зі збереженням пропорцій """
    self.logger.info('Запуск сервісу зміни розміру картинок')
    self.folder_service.create_base_folders()
    images_paths: List[str] = self.folder_service.get_all_file_paths(os.path.join(self.IMPORT_PATH, 'images'))
    for index, image_path in enumerate(images_paths, start=1):
      self.logger.info(f'Початок обробки картинки {index} з {len(images_paths)}: {os.path.basename(image_path)}')
    self.logger.success('Виконано')

    