from abc import ABC,abstractmethod 
from iloger import ilogger

class loggerFactory(ABC):
    
    @abstractmethod
    def createLogger(self) -> ilogger:
        pass