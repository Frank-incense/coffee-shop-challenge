from customer import Customer 

class TestCustomer:
    def test_instatiates_with_str(self):
        assert(Customer("Frank"))