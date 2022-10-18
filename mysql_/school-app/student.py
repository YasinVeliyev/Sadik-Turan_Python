class Student:
    def __init__(self, id: int | None, name: str, student_number: str, surname: str, birthdate: str, gender: str,
                 class_id: int):
        self.student_number = student_number
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.class_id = class_id
        self.id = id

    @staticmethod
    def create_students(students: [tuple]):
        return [Student(*student) for student in students]

    def __iter__(self):
        self.__index = 0
        self.__tuple = (
            self.name, self.student_number, self.surname, self.birthdate, self.gender, self.class_id, self.id)
        return self

    def __next__(self):
        if self.__index < len(self.__tuple):
            result = self.__tuple[self.__index]
            self.__index += 1
            if result:
                return result
            raise StopIteration
        raise StopIteration
