from module.folder.folder_service import FolderService
from module.logger.logger_service import LoggerService

logger = LoggerService('ImageForDatasetFile')
logger.success('Запуск підготовки зображень для датасуту')

folder_service = FolderService()
folder_service.create_base_folders()


