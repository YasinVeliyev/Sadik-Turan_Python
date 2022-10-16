import random


class Kart:
    def __init__(self, tip: str, deger: str):
        self.tip = tip
        self.deger = deger

    def karti_getir(self):
        return f"{self.tip} {self.deger}"

    def __repr__(self):
        return f"Kart(tip:{self.tip}, deger:{self.deger})"

    def __str__(self):
        return f"{self.tip} {self.deger}"


class Deste:
    tipler = ["karo", "sinek", "kupa", "maça"]
    degerler = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]

    def __init__(self):
        self.kartlar = [Kart(tip, deger) for tip in Deste.tipler for deger in Deste.degerler]

    def kart_sayisi(self):
        return len(self.kartlar)

    def kartlari_karistir(self):
        random.shuffle(self.kartlar)

    def kart_dagit(self, adet):
        adet = min(adet, self.kart_sayisi())
        if self.kart_sayisi() == 0:
            raise ValueError("Bütün kartlar dağıtıldı")
        kartlar, self.kartlar = self.kartlar[-adet:], self.kartlar[:-adet]
        return kartlar


# sinek5 = Kart("sinek", "5")
# sinekAs = Kart("karo", "A")
#
# print(repr(sinek5))
deste1 = Deste()
deste2 = Deste()
# print(deste2.kart_sayisi())
deste2.kartlari_karistir()
# print(deste2.kartlar)
print(deste2.kart_dagit(5))
print(deste2.kart_dagit(5))
print(deste2.kart_dagit(5))
print(deste2.kart_dagit(5))
print(deste2.kart_dagit(1))
print(deste2.kart_dagit(1))
print(deste2.kart_sayisi())
