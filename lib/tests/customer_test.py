from customer import Customer 
import pytest

class TestCustomer:
    def test_instatiates_with_str(self):
        '''instantiates with a single argument, a string.'''
        assert(Customer("Frank"))

    def test_name_is_is_valid(self):
        '''Name is a str between 1 and 15 characters in length.'''
        with pytest.raises(Exception):
            Customer(0)
            Customer("")

    def test_Customer_name_change(self):
        '''Customer class type checks name to be string.'''
        frank = Customer("Frank")
        with pytest.raises(Exception):
            frank.name = 0
            len(frank.name) == 0
            frank.name = " "