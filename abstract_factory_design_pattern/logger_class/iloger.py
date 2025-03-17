from abc import ABC,abstractmethod 

class ilogger(ABC):
    @abstractmethod 
    def log(self,msg : str) -> None: 
        pass 

    @abstractmethod
    def __del__(self):
        pass
    