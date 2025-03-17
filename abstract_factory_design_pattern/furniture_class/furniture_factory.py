from abc import ABC,abstractmethod 
import furniture_class


# Furniture factory
class furnitureFactory(ABC):
    @abstractmethod
    def createFurniture(self):
        pass 


# char factory 
class chairFactory(furnitureFactory):
    def createFurniture(self):
        return furniture_class.chair() 


# sofa factory 
class sofaFactory(furnitureFactory):
    def createFurniture(self):
        return furniture_class.sofa() 
    
# Table factory 

class tableFactory(furnitureFactory):
    def createFurniture(self):
        return furniture_class.table()