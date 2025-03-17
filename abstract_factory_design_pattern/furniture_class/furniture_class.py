from abc import ABC,abstractmethod 


# interface for futniture
class furniture(ABC):
    @abstractmethod
    def create(self,msg : str) -> None: 
        pass 



# Char class 
class chair(furniture):
    def create(self, msg : str) -> None:
        print(f"[INFO] : {msg}")


# Sofa class 
class sofa(furniture):
    def create(self, msg : str) -> None:
        print(f"[INFO] : {msg}")
    

# table class 
class table(furniture):
    def create(self, msg : str) -> None:
        print(f"[INFO] : {msg}")