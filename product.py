class Product:

    def __init__(self, name, quantity, pur_price, pay_price):
        self._name = name
        self._quantity = quantity
        self._pur_price = pur_price
        self._pay_price = pay_price

    @property
    def name(self):
        return self._name

    @property
    def pur_price(self):
        return self._pur_price

    @property
    def quantity(self):
        return self._quantity

    @property
    def pay_price(self):
        return self._pay_price

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
