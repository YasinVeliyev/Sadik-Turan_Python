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
    def __init__(self):
        pass

    @classmethod
    def connect(cls, username, password, database, auth_plugin="mysql_native_password", host="localhost"):
        cls.connection = mysql.connector.connect(host=host, user=username, password=password, auth_plugin=auth_plugin,
                                                 database=database)
        cls.cursor = cls.connection.cursor()
        return cls()

    def save_student(cls, StudentNumber: str, Name: str, Surname: str, Birthdate: str, GENDER: str):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,GENDER) VALUES(%s,%s,%s,%s,%s)"
        cls.cursor.execute(sql, (StudentNumber, Name, Surname, Birthdate, GENDER))

    def save_students(cls, students: list):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,GENDER) VALUES(%s,%s,%s,%s,%s)"
        cls.cursor.executemany(sql, students)

    @classmethod
    def get_students(cls):
        sql = "SELECT * FROM Student"
        cls.cursor.execute(sql)
        students = cls.cursor.fetchall()
        print(students)

    def __del__(self):
        try:
            Student.connection.commit()
        except Exception as err:
            print(err)
        finally:
            Student.connection.close()


student = Student.connect(username="yasinv", password=os.environ.get("DB_PASSWORD"), database="schooldb")
# student.save_students(ogrenciler)
# student.save_student("318", "Ali", "Cenk", datetime(2003, 8, 25), "E")
student.get_students()
