"""
    Implementation of Iterator design pattern 
    Example : Inventory 
"""


from abc import ABC,abstractmethod 
from typing import List

# Product class 
class Product:
    def __init__(self,p_name : str,p_price : float):
        self.p_name = p_name 
        self.p_price = p_price 

    def getName(self) -> str: 
        return self.p_name 

    def getPrice(self) -> float:
        return self.p_price 
    

# Interator interface 
class Iterator(ABC):
    @abstractmethod
    def first(self):
        pass 

    @abstractmethod
    def next_(self):
        pass 

    @abstractmethod 
    def hasNext(self):
        pass 


# Product iterator 
class productIterator(Iterator):
    def __init__(self,products : List):
        self.__prodcuts = products 
        self.__current = 0 
        self.__num_products = len(self.__prodcuts)

    def first(self) -> str: 
        if(self.__num_products <= 0):
            return None 
        return self.__prodcuts[self.__current] 
    
    def next_(self):
        if self.hasNext():
            self.__current += 1
            return self.__prodcuts[self.__current]
             
        return None 
    
    def hasNext(self) -> bool:
        if(self.__current + 1 < self.__num_products):
            return True 
        return False 
    

# Class for inventory 
class Inventory:
    
    def __init__(self):
        self.products : list  = [] 
    
    def  addProduct(self,product : Product):
        self.products.append(product)

    def createIterator(self):
        return productIterator(self.products) 
    

def main():
    # Create a product
    p1 = Product("Camera",25500.0)
    p2 = Product("Laptop",23453.00)
    p3 = Product("Mouse",244.00)
    p4 = Product("Speaker",546.00)

    # Add these product into inventory
    inventory : Inventory = Inventory() 
    inventory.addProduct(p1)
    inventory.addProduct(p2)
    inventory.addProduct(p3)
    inventory.addProduct(p4) 

    # Creater a inventory iterator ob
    iterator = inventory.createIterator()

    curr_product = iterator.first() 
    while curr_product:
        print(f"[INFO] Prodcut name : {curr_product.getName()} and prize : ${curr_product.getPrice()}")
        curr_product = iterator.next_()


if __name__ == "__main__":
    main()
        

