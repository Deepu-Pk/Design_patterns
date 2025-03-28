"""
    Implemetation of chain of responsibility 
    Example : Order validatation
"""

from abc import ABC,abstractmethod 

# Interface
class orderHadler(ABC):
    def __init__(self,next_handler = None):
        self.next_handler = next_handler 

    @abstractmethod
    def processOrder(self,order):
        pass 

# Order validatation class 
class orderValiidationHandler(orderHadler):
    def processOrder(self, order):
        print(f"[INFO] validating order : {order}")
    
        if self.next_handler != None: 
            self.next_handler.processOrder(order)

# Class for procecessing payament order
class processingPaymentHandler(orderHadler):
    def processOrder(self, order):
        print(f"[INFO] Processing payament for {order}")

        if self.next_handler != None: 
            self.next_handler.processOrder(order)

# Class for order prepration 
class orderPreprationHandler(orderHadler):
    def processOrder(self, order):
        print(f"[INFO] : Preparing order : {order}")

        if self.next_handler != None: 
            self.next_handler.processOrder(order)


# Delivery assignment class  
class deliveryAssignmentHandler(orderHadler):
    def processOrder(self, order):
        print(f"[INFO] : Your order : {order} is assigned to delivery person")

        if self.next_handler != None: 
            self.next_handler.processOrder(order)

# Order tracking handler 
class orderTackingHadler(orderHadler):
    def processOrder(self, order):
        print(f"[INFO] Your order : {order} is tracking")



def main():
    order_processing = orderValiidationHandler(
        next_handler = processingPaymentHandler(
            next_handler = orderPreprationHandler(
                next_handler = deliveryAssignmentHandler(
                    next_handler = orderTackingHadler()
                )
            )
        )
    )

    order = str(input("Plase enter your order : "))
    order_processing.processOrder(order)

if __name__ == "__main__":
    main()
    