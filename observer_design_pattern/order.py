"""
    Implemetation of oberserver design pattern 
    Example : Food order from online platform 
"""

from abc import ABC,abstractmethod 

class Observer(ABC):
    @abstractmethod
    def update(self,order):
        pass 



class Customer(Observer):
    
    def __init__(self,customer_name : str):
        self.customer_name = customer_name 

    def update(self,order):
        print(f"Hello {self.customer_name}! order #{order.order_id} is now {order.status}")


class Restaurant(Observer):
    def __init__(self,restaurant_name : str):
        self.restaurant_name = restaurant_name 
    
    def update(self,order):
        print(f"Hello {self.restaurant_name}! order #{order.order_id} is now {order.status}") 


class DeliveryPartner(Observer):
    def __init__(self,delivery_partner_name : str):
        self.delivery_partner_name = delivery_partner_name 

    def  update(self,order):
        print(f"Hi {self.delivery_partner_name}! order #{order.order_id} is now {order.status}")
    
class CallCenter(Observer):
    def update(self,order):
        print(f"Call center ! order #{order.order_id} is now {order.status}")



class Order:
    def __init__(self,order_id : int):
        self.order_id = order_id 
        self.status = "Order placed"
        self.observers = []

    def getID(self) -> int:
        return self.order_id

    def setStatus(self,new_Status : str):
        self.status = new_Status
        self.notifyObservers()

    def attach(self,observer : Observer):
        self.observers.append(observer) 

    def dettach(self,observer : Observer):
        if observer in self.observers:
            self.observers.remove(observer) 
        
    
    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self) 
    
        print('+'*60)


def main():

    # Create an order 
    order = Order(500)

    # Create customers,resaturant,derivers and call center 
    customer = Customer("Deepak") 
    driver = DeliveryPartner("Ramesh")
    restaurant = Restaurant("Tea Spot")
    callcenter = CallCenter()  

    order.attach(customer)
    order.attach(driver)
    order.attach(restaurant)
    order.attach(callcenter) 


    order.setStatus("Out of delivery")

    order.setStatus("Order is misplaced")

    order.setStatus("Order is deliverd")




if(__name__ == "__main__"):
    main()


