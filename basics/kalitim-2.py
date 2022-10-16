class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person nesnesi türedildi")


class Student(Person):
    def __init__(self):
        pass


class Teacher(Person):
    pass


s = Student("Yasin", "Veliyev", 30)
print(s.name)
