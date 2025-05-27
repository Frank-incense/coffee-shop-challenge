from customer import Customer
from coffee import Coffee

class Order:
    all = []
    def __init__(self, customer, coffee, price):
        if isinstance(customer, Customer) and \
              isinstance(coffee, Coffee) and \
                isinstance(price, float) and \
                    0.9 < price < 10.1:
            self.customer = customer
            self.coffee = coffee
            self._price = price
            type(self).all.append(self)
        else:
            raise ValueError("Ensure arguments are of the correct type")
    
    @property   
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        raise ValueError("Price cannot be changed once initialised")