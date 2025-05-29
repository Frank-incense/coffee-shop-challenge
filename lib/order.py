from customer import Customer
from coffee import Coffee

class Order:
    all = []
    def __init__(self, customer, coffee, price):
        if isinstance(price, float) and 0.9 < price < 10.1:
            self.customer = customer
            self.coffee = coffee
            self._price = price
            type(self).all.append(self)
        else:
            raise ValueError(f"{price} should be a number 0.9 < price < 10.1 ")
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise TypeError("Ensure arguments are of the correct type")
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise TypeError("Ensure arguments are of the correct type")
        
    @property   
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        raise AttributeError("Price cannot be changed once initialised")