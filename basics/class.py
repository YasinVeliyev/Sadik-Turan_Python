class Ogrenci:
    pass


ogrenci = Ogrenci()
ogrenci1 = Ogrenci()


# print(ogrenci,ogrenci1,sep="\n")

class Product:
    pass


p1 = Product()
p2 = Product()
p3 = Product()
products = [p1, p2, p3]

for p in products:
    print(p, type(p))
