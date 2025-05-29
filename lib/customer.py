class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) < 16:
            self._name = name
        else:
            raise ValueError(f"{name} must be a string of length 1 - 15 ")
        
    def orders(self):
        from order import Order
        return [order for order in Order.all if self == order.customer]
    

    def coffees(self):
        from order import Order
        return [order.coffee for order in Order.all if self == order.customer]
    
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        coffee_orders = [orders for orders in Order.all if coffee == orders.coffee]
        customers = {}
        max = 0
        result = None
        for coffee in coffee_orders:
            if coffee.customer:
                max += 1
                customers[coffee.customer] = max
            else:
                max = 1
                customers[coffee.customer] = max

        for key, val in customers.items():
            print(val)
            if max <= val:
                max = val
                result = key
        
        return result
    
