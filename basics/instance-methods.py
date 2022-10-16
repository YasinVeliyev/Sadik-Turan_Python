class Person:
    def __init__(self, name: str, surname: str, year: int):
        self.name = name
        self.surname = surname
        self.year = year

    def intro(self):
        return f"Benim adım {self.name} ve Soyadim {self.surname}"

    def calculate_age(self):
        return f"{2022 - self.year}"


p1 = Person("Yasin", "Veliyev", 1992)
print(p1.intro(), "Ve menim ", p1.calculate_age(), "yasim var")
