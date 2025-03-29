"""
    Combination of factory design pattern and strategy design pattern 
    Example : Payament procesing system
"""

from abc import ABC,abstractmethod 

# Abstract class for payment strategy
class paymentStrategy(ABC):
    @abstractmethod 
    def processPayament(self,amount : float):
        pass 

    def __del__(self):
        print(f"[INFO] : {self.__class__.__name__} instance is cleared")


# creadit card payament strategy 
class creditCardPayament(paymentStrategy):
    def processPayament(self, amount : float):
        print(f"[INFO] : Credict card transaction : {amount} ")


# netbanking payment strategy 
class netbankingPayment(paymentStrategy):
    def processPayament(self, amount : float):
        print(f"[INFO] : netbanking payament transaction : {amount}")

# Gpay payament startegy 
class gpayPayment(paymentStrategy):
    def processPayament(self, amount : float):
        print(f"[INFO] : Gpay payment transaction : {amount}")


# Factory design pattern
def factoryMethod(payment_type : str):
    if payment_type == "credictcard":
        return creditCardPayament()
    elif payment_type == "gpay":
        return gpayPayment() 
    elif payment_type == "netbanking":
        return netbankingPayment() 
    else:
        return gpayPayment()

class paymentProcessor:
    def __init__(self):
        self.__payement_method = None 

    def setPaymentMethod(self,paymet_method : str):
        if self.__payement_method:
            del self.__payement_method 
        self.__payement_method = factoryMethod(paymet_method)
    
    def processPayament(self,amount : float):
        self.__payement_method.processPayament(amount)

    def __del__(self):
        del self.__payement_method 



def main():
    payment_processor = paymentProcessor() 
    
    # Credit card payament mehthod 
    payment_processor.setPaymentMethod("credictcard")
    payment_processor.processPayament(1231.00)

    # Netbanking payament
    payment_processor.setPaymentMethod("netbanking")
    payment_processor.processPayament(121314.00)

    # Gpay payment method 
    payment_processor.setPaymentMethod("gpay")
    payment_processor.processPayament(3454252.00)

if __name__ == "__main__":
    main()