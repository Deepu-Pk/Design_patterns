"""
    Implemetation of payment gateway class
    Only one object can created (Singleton design pattern)
"""

import threading 

class paymentGateway:
    __instance = None 
    __lock = threading.Lock() 

    # Singleton design pattern
    def __new__(cls):
        if cls.__instance is None: # Double check locking
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(paymentGateway,cls).__new__(cls)
                    print(f"Payment gateway is intialized")
        return cls.__instance 
        
    
    def processPayment(self, amount : float) -> None: 
        print(f"Processing the amnount : ${amount}")


def main() -> None:
    ob = paymentGateway() 
    ob.processPayment(300.00)

    another_ob = paymentGateway() 
    if(another_ob == ob):
        print(f"Both object are same")
    else:
        print(f"Both object are not same")


if(__name__ == "__main__"):
    main()
