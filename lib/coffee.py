class Coffee:
    all = []
    def __init__(self, name):
        if len(name) > 2:
            self._name = name
            type(self).all.append(self)
        else:
            raise Exception("Name should be atleast 3 chararcters.")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        raise Exception(f"Name can not be changed once initialised")
    
    def orders(self):
        from order import Order
        return [orders for orders in Order.all if self == orders.coffee]
    
    def customers(self):
        from order import Order
        return [orders.customer for orders in Order.all if self == orders.coffee]
    
    def num_orders(self):
        from order import Order
        return len([order for order in Order.all if self == order.coffee])
    
    def average_price(self):
        from order import Order
        average = 0
        count = 0
        for orders in Order.all:
            if self == orders.coffee:
                average += orders.price
                count += 1 
        if count == 0:
            return 0
        return average / count