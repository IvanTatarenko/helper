import os
from services.logger.logger_service import LoggerService

class FolderService:
  def __init__(self):
    self.EXPORT_PATH = os.path.abspath('export')
    self.IMPORT_PATH = os.path.abspath('import')
    self.logger = LoggerService(FolderService.__name__)

  def __exists_folder(self, path):
    """Перевірка чи існує папка"""
    if not os.path.exists(path):
      self.logger.info(f"Папка не існує: {path}")
      return False
    else:
      self.logger.info(f"Папка вже існує: {path}")
      return True

  def __create_folder(self, path):
    """Створення папки якщо вона не існує"""
    if not self.__exists_folder(path):
      os.makedirs(path)
      self.logger.success(f"Папка створена: {path}")

  def create_folder_for_export(self, folder_name):
    """Створення папки в папці export"""
    full_path = os.path.join(self.EXPORT_PATH, folder_name)
    self.__create_folder(full_path)

  def create_folder_for_import(self, folder_name):
    """Створення папки в папці import"""
    full_path = os.path.join(self.IMPORT_PATH, folder_name)
    self.__create_folder(full_path)

  def create_base_folders(self):
    """Створення базового набору папок"""
    self.create_folder_for_export('images/800px')
    self.create_folder_for_import('images')