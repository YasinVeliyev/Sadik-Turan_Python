class Let:
    pass


class Pet:
    cinsler = ["kedi", "kopek", "kus"]

    @classmethod
    def display_cinsler(cls):
        print(cls.cinsler)

    def __new__(cls, *args, **kwargs):
        if args[1] not in cls.cinsler:
            raise ValueError(f"{args[1]} bir evcil hayvan deyildir")
        return super().__new__(cls)

    def __init__(self, isim, cins):
        self.isim = isim
        self.cins = cins


boncuk = Pet("Boncuk", "kedi")
pasa = Pet("Paşa", "kopek")
mavis = Pet("Mavvis", "kus")

print(boncuk.isim)
print(pasa.display_cinsler())
print(mavis)
