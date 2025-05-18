from customer import Customer
from order import Order
from coffee import Coffee
import pytest

class TestCoffee:
    def test_instantiates_with_str(self):
        '''instantiates with a single argument, a string.'''
        assert(Coffee("ben"))

    def test_validates_name(self):
        """Coffee class Validates name has atleast 3 chars."""
        with pytest.raises(Exception):
            Coffee("na")

    def test_name_is_immutable(self):
        """Coffee class name is immutable once initialised."""
        bean = Coffee("name")
        with pytest.raises(Exception):
            bean.name = "Other name"

    def test_coffee_has_orders(self):
        '''Test Coffee class has method orders that returns list of orders'''
        frank = Customer("Frank")
        espresso = Coffee("Espresso")
        price = 10.0

        order = Order(frank, espresso, price)

        assert espresso.orders() == [order]

    def test_coffee_has_coffees(self):
        '''Test Coffee class has method orders that retruns list of orders'''
        frank = Customer("Frank")
        espresso = Coffee("Espresso")
        price = 10.0

        Order(frank, espresso, price)

        assert frank in espresso.customers()

    def test_coffee_returns_no_of_orders(self):
        '''Coffee class has method num_orders that returns total count of orders for coffee instance'''
        espresso = Coffee("Espresso")
        latte = Coffee("Latte")
        price = 10.0
        customer1 = Customer("customer1")
        customer2 = Customer("customer2")
        customer3 = Customer("customer3")

        Order(customer1, espresso, price)
        Order(customer2, espresso, price)
        Order(customer3, espresso, price)

        assert espresso.num_orders() == 3
        assert latte.num_orders() == 0

    def test_coffee_average_price(self):
        '''Coffee class calculates average price for this instance'''
        espresso = Coffee("Espresso")
        latte = Coffee("Latte")
        price = 10.0
        customer1 = Customer("customer1")
        customer2 = Customer("customer2")
        customer3 = Customer("customer3")

        Order(customer1, espresso, price)
        Order(customer2, espresso, 9.5)
        Order(customer3, espresso, 6.5)

        assert espresso.average_price() == (price + 9.5 + 6.5) / 3
        assert latte.average_price() == 0