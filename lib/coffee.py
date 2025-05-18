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
        raise Exception(f"Name cann not be changed once initialised")