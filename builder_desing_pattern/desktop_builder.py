from abc import ABC,abstractmethod 
from desktop import Desktop

class desktopBuilder(ABC):
    def __init__(self):
        self._desktop = Desktop() 
    
    @abstractmethod
    def buildMotherboard(self):
        pass 

    @abstractmethod
    def buildProcessor(self):
        pass 
    
    @abstractmethod
    def buildMemory(self):
        pass 

    @abstractmethod
    def buildStograge(self):
        pass 

    @abstractmethod
    def buildGraphicCard(self):
        pass 

    def getDesktop(self):
        return self._desktop