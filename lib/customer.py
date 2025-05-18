class Customer:
    all = []
    def __init__(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
            type(self).all.append(self)
        else:
            raise Exception(f"{name} must be a string of length 1 - 15 ")
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) < 16:
            self._name = name
        else:
            raise Exception(f"{name} must be a string of length 1 - 15 ")
        
    def orders(self):
        from order import Order
        return [order for order in Order.all if self == order.customer]
    

    def coffees(self):
        from order import Order
        return [order.coffee for order in Order.all if self == order.customer]
    
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
        