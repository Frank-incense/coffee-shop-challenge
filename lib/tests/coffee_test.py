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
