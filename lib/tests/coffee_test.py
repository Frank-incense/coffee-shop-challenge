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
        from customer import Customer
        from order import Order

        frank = Customer("Frank")
        espresso = Coffee("Espresso")
        price = 10.0

        order = Order(frank, espresso, price)

        assert espresso.orders() == [order]

    def test_coffee_has_coffees(self):
        '''Test Coffee class has method orders that retruns list of orders'''
        from customer import Customer
        from order import Order

        frank = Customer("Frank")
        espresso = Coffee("Espresso")
        price = 10.0

        Order(frank, espresso, price)

        assert frank in espresso.customers()

    