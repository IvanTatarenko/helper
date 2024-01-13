import os

class FolderService:
  def __init__(self):
    pass

  def __exists_folder(self, path):
    """Перевірка чи існує папка"""
    if not os.path.exists(path):
      print(f"Папка не існує: {path}")
      return True
    else:
      print(f"Папка вже існує: {path}")
      return False

  def __create_folder(self, path):
    """Створення папки якщо вона не існує"""
    if not self.__exists_folder(path):
      os.makedirs(path)
      print(f"Папка створена: {path}")

  def create_folder_for_export(self, folder_name):
    EXPORT_PATH = os.path.abspath('export')
    full_path = os.path.join(EXPORT_PATH, folder_name)
    self.__create_folder(full_path)
