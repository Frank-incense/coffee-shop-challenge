from order import Order
from customer import Customer
from coffee import Coffee
import pytest

class TestOrder:
    def test_order_init(self):
        '''Order takes Customer instance as an argument'''
        frank = Customer("Frank")
        espresso = Coffee("Espresso")
        price = 10.0
        order = Order(frank, espresso, price)

        assert order.customer == frank
        assert order.coffee == espresso
        assert order.price == price

    def test_order_validates_customer(self):
        '''Test order class validates customer type'''
        espresso = Coffee("Espresso")
        price = 10.0

        with pytest.raises(Exception):
            Order("frank", espresso, price)
    
    def test_order_validates_coffee(self):
        '''Test order class validates coffee type'''
        frank = Customer("Frank")
        price = 10.0

        with pytest.raises(Exception):
            Order(frank, "espresso", price)

    def test_order_validates_price(self):
        '''Test order class validates price'''
        frank = Customer("Frank")
        espresso = Coffee("Espresso")
        price = 10

        with pytest.raises(Exception):
            Order(frank, espresso, price)
        with pytest.raises(Exception):
            Order(frank, espresso, "price")
    
    def test_order_validates_price_amount(self):
        '''Test order class validates price amount'''
        frank = Customer("Frank")
        espresso = Coffee("Espresso")
        price = 11.0
        
        with pytest.raises(Exception):
            Order(frank, espresso, price)
    
    def test_order_price_immutable(self):
        '''Test order class price is immutable once initialised'''
        frank = Customer("Frank")
        espresso = Coffee("Espresso")
        price = 10.0
        order = Order(frank, espresso, price)
        
        with pytest.raises(Exception):
            order.price = 5.0

