import os
from datetime import datetime

import mysql.connector
from dotenv import load_dotenv

load_dotenv("/home/yasin/Udemy/SadikTuranPython/.env")

ogrenciler = [
    ("307", "Ahmet", "Yılmaz", datetime(2005, 5, 17), "E"),
    ("308", "Ali", "Can", datetime(2005, 6, 17), "E"),
    ("309", "Canan", "Tan", datetime(2005, 7, 7), "K"),
    ("310", "Ayşe", "Taner", datetime(2005, 9, 23), "K"),
    ("311", "Bahadır", "Toksöz", datetime(2004, 7, 27), "E"),
    ("312", "Ali", "Cenk", datetime(2003, 8, 25), "E")
]


class Student:
    def __new__(cls, user, password, database, auth_plugin="mysql_native_password", host="localhost"):
        cls.connection = mysql.connector.connect(user=user, password=password, database=database,
                                                 auth_plugin="mysql_native_password",
                                                 host="localhost")
        cls.cursor = cls.connection.cursor()
        return super(Student, cls).__new__(cls)

    @classmethod
    def connect(cls, user, password, database, auth_plugin="mysql_native_password", host="localhost"):
        cls.connection = mysql.connector.connect(host=host, user=user, password=password, auth_plugin=auth_plugin,
                                                 database=database)
        cls.cursor = cls.connection.cursor()
        return cls()

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def save_student(cls, StudentNumber: str, Name: str, Surname: str, Birthdate: str, GENDER: str):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,GENDER) VALUES(%s,%s,%s,%s,%s)"
        cls.cursor.execute(sql, (StudentNumber, Name, Surname, Birthdate, GENDER))
        cls.commit()

    @classmethod
    def save_students(cls, students: list):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,GENDER) VALUES(%s,%s,%s,%s,%s)"
        cls.cursor.executemany(sql, students)
        cls.commit()

    @classmethod
    def get_students(cls):
        sql = "SELECT * FROM Student"
        cls.cursor.execute(sql)
        students = cls.cursor.fetchall()
        print(students)

    @classmethod
    def get_student_by_id(cls, id):
        sql = "SELECT * FROM Student WHERE id=%s;"
        cls.cursor.execute(sql, (id,))
        try:
            return cls.cursor.fetchone()
        except Exception as err:
            print(err)
        finally:
            cls.connection.close()

    @classmethod
    def update_student(cls, StudentNumber: str, Name: str, Surname: str, Birthdate: str, GENDER: str):
        sql = "UPDATE Student set StudentNumber=%s,Name=%s,Surname=%s,Birthdate=%s,GENDER=%s"
        cls.cursor.execute(sql, (StudentNumber, Name, Surname, Birthdate, GENDER))
        cls.commit()

    @classmethod
    def commit(cls):
        try:
            cls.connection.commit()
        except Exception as err:
            print(err)

    def __del__(self):
        print("Hi")
        try:
            from mysql.connector.locales.eng import client_error
            self.connection.close()
        except Exception as err:
            print(err)


student = Student(host="localhost", user="yasinv", password=os.environ.get("DB_PASSWORD"),
                  auth_plugin='mysql_native_password', database="schooldb")
# student.save_students(ogrenciler)
# student.save_student("323", "Ali", "Cenk", datetime(2003, 8, 25), "E")
print(student.get_student_by_id(1))
