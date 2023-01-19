from product import Product

class Store:
    def __init__(self, balance):
        self._balance = balance
        self._products = []
        pass

    @property
    def balance(self):
        return self._balance

    @property
    def products(self):
        return self._products

    @balance.setter
    def balance(self, value):
        self._balance = value

    def add_product(self, name, quantity, purPrice, payPrice):
        if self.balance >= purPrice * quantity:
            self.products.append(Product(name, quantity, purPrice, payPrice))
            self.balance -= purPrice * quantity
            print(f'{quantity} {name} product added ')
        else:
            print("Your balance is not ready for that quantity! ")

    def sell_product(self, name, quantity):
        for product in self._products:
            if product.name == name:
                if product.quantity >= quantity:
                    self.balance += product.pay_price
                    product.quantity -= quantity
                    if product.quantity == 0:
                        self.products.remove(product)
                else:
                    print(f'Theres not {quantity} count of {name}')
            else:
                print(f'{name} product not found')

    def profit(self):
        temp = 0
        for prod in self.products:
            temp += (prod.quantity * prod.pay_price) - (prod.quantity * prod.pur_price)
        return temp

    def filter_by_letter(self):
        length = len(self.products)

        for ind in range(length):
            min_index = ind

            for j in range(ind + 1, length):
                if self.products[j].name[0] < self.products[min_index].name[0]:
                    min_index = j
                (self.products[ind], self.products[min_index]) = (self.products[min_index], self.products[ind])
        pass

    def filter_by_quantity(self):
        length = len(self.products)

        for ind in range(length):
            min_index = ind

            for j in range(ind + 1, length):
                if self.products[j].quantity < self.products[min_index].quantity:
                    min_index = j
            (self.products[ind], self.products[min_index]) = (self.products[min_index], self.products[ind])

    def filter_by_price(self):
        length = len(self.products)

        for ind in range(length):
            min_index = ind

            for j in range(ind + 1, length):
                if self.products[j].pay_price < self.products[min_index].pay_price:
                    min_index = j
            (self.products[ind], self.products[min_index]) = (self.products[min_index], self.products[ind])

    def filter_by_mode(self):
        mode = input("Enter l for letters q for quantity and p for price")
        if mode == "l":
            self.filter_by_letter()
        elif mode == "q":
            self.filter_by_quantity()
        elif mode == "p":
            self.filter_by_price()
        else:
            print("Invalid option")
