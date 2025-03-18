"""
    Implementation of product prototype 
"""


from abc import ABC,abstractmethod 

class productPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass 

    @abstractmethod
    def display(self):
        pass 



class product(productPrototype):
    def __init__(self,name : str , price : float): 
        self.name = name 
        self.price = price


    def clone(self):
        return product(self.name,self.price) 


    def display(self):
        print(f"Name : {self.name}")
        print(f"Price : {self.price}") 




def main():
    p = product("HP Laptop",65000.00)
    print(f"== Product details ==")
    p.display() 

    p_clone = p.clone() 
    print(f"== Cloned product details ==")
    p_clone.display()

if(__name__ == "__main__"):
    main()