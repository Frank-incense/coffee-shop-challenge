from customer import Customer
from coffee import Coffee
from order import Order
import pytest

class TestCustomer:
    def test_instatiates_with_str(self):
        '''instantiates with a single argument, a string.'''
        assert(Customer("Frank"))

    def test_name_is_is_valid(self):
        '''Name is a string between 1 and 15 characters in length.'''
        with pytest.raises(ValueError):
            Customer(0)
        with pytest.raises(ValueError):
            Customer("")

    def test_Customer_name_change(self):
        '''Customer class type checks name to be string.'''
        frank = Customer("Frank")
    
        with pytest.raises(ValueError):
            frank.name = 0
            len(frank.name) == 0
            frank.name = " "

    def test_customer_has_orders(self):
        '''Test Customer class has method orders that retruns list of orders'''
        frank = Customer("Frank")
        espresso = Coffee("Espresso")
        price = 10.0

        order = Order(frank, espresso, price)

        assert frank.orders() == [order]

    def test_customer_has_coffees(self):
        '''Test Customer class has method orders that retruns list of orders'''
        frank = Customer("Frank")
        espresso = Coffee("Espresso")
        price = 10.0

        Order(frank, espresso, price)

        assert espresso in frank.coffees()

    def test_customer_can_create_order(self):
        '''Customer has method create_order that intantiates a new order'''
        frank = Customer("Frank")
        espresso = Coffee("Espresso")
        price = 10.0

        assert frank.create_order(espresso, price) in Order.all

    def test_customer_has_most_aficionado(self):
        '''
        Customer has method most_aficionado that 
        returns the customer who spent the most on 
        a given coffee.
        '''
        espresso = Coffee("Espresso")
        latte = Coffee("Latte")
        price = 10.0
        customer1 = Customer("customer1")
        customer3 = Customer("customer3")

        Order(customer1, espresso, price)
        Order(customer1, espresso, price)
        Order(customer3, latte, 6.5)

        assert Customer.most_aficionado(espresso) == customer1