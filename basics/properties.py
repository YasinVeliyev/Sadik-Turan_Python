class Price:
    def __init__(self, price=0):
        self.price = price

    def __get__(self, instance, owner):
        return self.price

    def __set__(self, instance, price):
        if price < 0:
            raise ValueError("Fiyat 0-dan küçük ola bilməz")
        self.price = price


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Fiyat 0-dan küçük ola bilməz")
        self._price = price


p1 = Product("Nokia G20", 370)
p = Product("Iphone 12", 2140.0)

print(p1.price, p.price)
