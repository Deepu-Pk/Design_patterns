"""
    Impelementation of tempalte design pattern 
    Example : Internation and local order from any online store 
"""

from abc import abstractmethod,ABC 

# Absatract class for order processing template
class orderProcessingTemplate(ABC):
    def processOrder(self):
        self.verifyOrder()
        self.assignDeliveryAgent()
        self.trackDelivery()
    
    @abstractmethod
    def verifyOrder(self):
        pass 

    @abstractmethod
    def assignDeliveryAgent(self):
        pass 

    @abstractmethod
    def trackDelivery(self):
        pass 

#Local order system 
class localOrderPorcessor(orderProcessingTemplate):
    def verifyOrder(self):
        print(f"[INFO] : Verifying local order")

    def assignDeliveryAgent(self):
        print(f"[INFO] : Assigning local delivey agent")
    
    def trackDelivery(self):
        print(f"[INFO] : Tracking  local delivery")


class internationOrderProcessor(orderProcessingTemplate):

    def verifyOrder(self):
        print(f"[INFO] : Verifying international order")

    def assignDeliveryAgent(self):
        print(f"[INFO] : Assigning local internation agent")
    
    def trackDelivery(self):
        print(f"[INFO] : Tracking  internationl delivery")


def main():
    # Local order
    local_order = localOrderPorcessor()
    local_order.processOrder() 

    # Internationl order 
    international_order = internationOrderProcessor() 
    international_order.processOrder()

if(__name__ == "__main__"):
    main()

