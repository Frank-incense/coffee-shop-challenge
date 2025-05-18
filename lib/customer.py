class Customer:
    all = []
    def __init__(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
            type(self).all.append(self)
        else:
            raise Exception(f"{name} must be a string of length 1 - 15 ")
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 0 < len(name) < 16:
            self._name = name
        else:
            raise Exception(f"{name} must be a string of length 1 - 15 ")