from services.folder.folder_service import FolderService
from services.logger.logger_service import LoggerService

logger = LoggerService('ImageForDatasetFile')
logger.success('Запуск підготовки зображень для датасету')

folder_service = FolderService()
folder_service.create_base_folders()


