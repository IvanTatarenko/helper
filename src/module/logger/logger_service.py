import logging
from datetime import datetime

# Клас для кольорового логування
class LoggerService:
    def __init__(self, class_name):
        self.class_name = class_name

    def info(self, message):
        self.__log("INFO   ", message, "\033[94m") 

    def success(self, message):
        self.__log("SUCCESS", message, "\033[92m")

    def err(self, message):
        self.__log("ERROR  ", message, "\033[91m")

    def warning(self, message):
        self.__log("WARNING", message, "\033[93m")

    def __log(self, level, message, color_code):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{color_code}[{time} - {self.class_name} - {level}] {message}\033[0m"
        print(formatted_message)


