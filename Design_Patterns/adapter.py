from abc import ABC, abstractmethod
from pyfiglet import figlet_format

object = "Hello"

class Logger(ABC):
    @abstractmethod
    def log(self, obj):
        pass

class ConsoleLogger(Logger):
    def log(self, obj):
        print(obj)


class PyfigletLogger(Logger):
    def __init__(self):
        self.logger = ConsoleLogger()

    def log(self, obj):
        self.logger.log(figlet_format(object))

logger = PyfigletLogger()
logger.log(object)



