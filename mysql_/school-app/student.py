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
