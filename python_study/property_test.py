class property_test:

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

p_t = property_test()
p_t.name = 'ddc'
print(p_t.name)