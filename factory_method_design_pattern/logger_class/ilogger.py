
"""
    Absatrct class for logger
"""

from abc import ABC,abstractmethod
class ilogger(ABC):
    @abstractmethod
    def log(self,string : str) -> None:
        pass 
    @abstractmethod
    def __del__(self):
        pass 

