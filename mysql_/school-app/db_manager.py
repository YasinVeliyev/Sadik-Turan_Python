import os

import mysql.connector
from dotenv import load_dotenv

from class_ import Class
from class_lesson import Class_Lesson
from student import Student
from teacher import Teacher

load_dotenv("../../.env")


class Db_Manager:
    def __init__(self, host="localhost", user="yasinv", password=os.environ.get("DB_PASSWORD"), database="schooldb",
                 auth_plugin="mysql_native_password"):
        self.connection = mysql.connector.connect(host=host, user=user, password=password, database=database,
                                                  auth_plugin=auth_plugin)
        self.cursor = self.connection.cursor()

    def get_student_by_id(self, id: int):
        sql = "SELECT * FROM Student WHERE id = %s"
        self.cursor.execute(sql, (id,))
        try:
            student = self.cursor.fetchone()
            return Student(*student)
        except Exception as err:
            print("Error: ", err)

    def get_students_by_class_id(self, id: int):
        sql = "SELECT * FROM Student WHERE class_id = %s"
        self.cursor.execute(sql, (id,))
        try:
            students = self.cursor.fetchall()
            return Student.create_students(students)
        except Exception as err:
            print("Error: ", err)

    def add_student(self, student: Student):
        sql = "INSERT INTO Student(name, student_number, surname, birth_date, gender,class_id) VALUES(%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql, (*student,))
        self.connection.commit()

    def edit_student(self, student: Student):
        sql = "UPDATE  Student SET name=%s, student_number=%s, surname=%s, birth_date=%s, gender=%s,class_id=%s WHERE id=%s;"
        self.cursor.execute(sql, (*student,))
        self.connection.commit()

    def delete_student(self, id: int):
        sql = "DELETE FROM Student WHERE id=%s;"
        self.cursor.execute(sql, (id,))
        self.connection.commit()

    def add_or_edit_student(self, student: Student):
        pass

    def add_teacher(self, teacher: Teacher):
        sql = "INSERT INTO Teacher(branch, name, surname, birthdate, gender) VALUES(%s,%s,%s,%s,%s)"
        # self.cursor.execute(sql, (
        #     student.name, student.student_number, student.surname, student.birthdate, student.gender, student.class_id))
        # self.connection.commit()

    def edit_teacher(self, teacher):
        pass

    def get_classes(self):
        sql = "SELECT * FROM Class"
        self.cursor.execute(sql)
        try:
            classes = self.cursor.fetchall()
            return Class.create_class(classes)
        except Exception as err:
            print("Error: ", err)

    def add_class(self, class_: Class):
        pass

    def edit_class(self, class_):
        pass

    def add_class_lesson(self, class_lesson: Class_Lesson):
        pass

    def edit_class_lesson(self, class_lesson):
        pass

    def __del__(self):
        self.connection.commit()
        self.connection.close()
        print("Database əlaqəsi kəsildi")


if __name__ == "__main__":
    manager = Db_Manager()
    # student = manager.get_student_by_id(1)
    # students = manager.get_students_by_class_id(1)
    # print(*[student.__dict__ for student in students], sep="\n")
    newstudent = Student(None, "Asim", 6589, "Veliyev", "1985-12-17", "E", 3)
    # print(next(newstudent))
    manager.add_student(newstudent)
    # manager.edit_student(Student(6, "Alı", 312, "Ceng", "1992-12-17", "E", 2))
