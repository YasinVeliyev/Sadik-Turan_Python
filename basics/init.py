class Product:
    def __init__(self, name, price, isActive=False):
        self.name = name
        self.price = price
        self.isActive = isActive
        print("Product nesnesi olusduruldu")


p1 = Product("Samsung S10", 2000, True)
p2 = Product("Iphone 8", 2500, False)

print(p1.price, p2)
