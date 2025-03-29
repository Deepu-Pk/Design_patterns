"""
    Implemetation of stategy design pattern 
    Example : Online payment system
"""

from abc import ABC,abstractmethod

# Payment class interface
class paymentStrategy(ABC):
    @abstractmethod
    def processPayment(self,amount : float):
        pass 

    def __del__(self):
        print(f"[INFO] : Deleteing the {self.__class__.__name__} instance")
    
# Creadicard payment system
class credictCardPayment(paymentStrategy):
    def processPayment(self, amount):
        print(f"[INFO] : Processing credict card payment of {amount}")
    

# Gapy payment system
class gpayPayament(paymentStrategy):
    def processPayment(self, amount):
        print(f"[INFO] : Processing Gpay payement of {amount}")


# netbanking payment system 
class netBankPayament(paymentStrategy):
    def processPayment(self, amount):
        print(f"[INFO] : Processing internet baking payament of {amount}")


# Payment processor 

class payamentProcessor:
    def __init__(self):
        self.__payament_strategy = None 
    
    def setPayamentStrategy(self,strategy : paymentStrategy):
        if self.__payament_strategy:
            del self.__payament_strategy 
        self.__payament_strategy = strategy 

    def processPayament(self,amount : float):
        if self.__payament_strategy:
            self.__payament_strategy.processPayment(amount)
        else: 
            print(f"[ERROR] : Payament method is not set")

    def __del__(self):
        if self.__payament_strategy:
            del self.__payament_strategy 
        print(f"[INFO] : Cleaning up payament method instance")


def main():
    processor = payamentProcessor()

    # creadit card payment system 
    strategy = credictCardPayment()
    processor.setPayamentStrategy(strategy)
    processor.processPayament(1024.00)

    # Gpay payament method 
    strategy = gpayPayament() 
    processor.setPayamentStrategy(strategy)
    processor.processPayament(3355.00)

    #Internet payament method 
    strategy = netBankPayament() 
    processor.setPayamentStrategy(strategy)
    processor.processPayament(42525.00)


if __name__ == "__main__":
    main()