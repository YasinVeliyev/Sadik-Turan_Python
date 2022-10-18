import datetime

from db_manager import Db_Manager
from student import Student


class App:
    def __init__(self):
        self.db = Db_Manager()

    def add_student(self):
        self.display_classes()
        class_id = int(input("Hangi Sinif? "))
        student_number = input("Öğrenci Numarası? ")
        name = input("İsim? ")
        surname = input("Soyad? ")
        birthdate = datetime.date.fromisoformat(input("Doğum tarihi (Yıl-ay-gün)? "))
        gender = input("Cinsiyet (E/K)? ")
        student = Student(None, name, student_number, surname, birthdate, gender, class_id)
        self.db.add_student(student)

    def delete_student(self):
        self.display_students()
        id = int(input("Öğrenic İd? "))
        self.db.delete_student(id)

    def edit_student(self):
        self.display_students()
        id = int(input("Öğrenic İd? "))
        student = self.db.get_student_by_id(id)
        student.class_id = int(input(f"Sinif? ")) or student.class_id
        student.student_number = input("Öğrenci Numarası? ") or student.student_number
        student.name = input("İsim? ") or student.name
        student.surname = input("Soyad? ") or student.surname
        student.birthdate = datetime.date.fromisoformat(input("Doğum tarihi (Yıl-ay-gün)? ")) or student.birthdate
        student.gender = input("Cinsiyet (E/K)? ") or student.gender
        self.db.edit_student(student)

    def display_classes(self):
        classes = self.db.get_classes()
        print("Sınıflar".center(30, "="))
        for class_ in classes:
            s = f"| {class_.id}: {class_.name}"
            print(s.ljust(29), "|")
        print("=" * 30)

    def display_students(self):
        self.display_classes()
        class_id = int(input("Hangi Sinif? "))
        students = self.db.get_students_by_class_id(class_id)
        print("Öğrenci Listesi".center(30, "="))
        for student in students:
            s = f"| {student.id}. {student.name} {student.surname}"
            print(s.ljust(29), "|")
        print("=" * 30)

    def init_app(self):
        msg = "1-Öğrenci Listesi\n2-Öğrenci ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E\Ç)"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == "1":
                self.display_students()
            elif islem == "2":
                self.add_student()
            elif islem == "3":
                self.edit_student()
            elif islem == "4":
                self.delete_student()
            elif islem == "5":
                pass
            elif islem == "6":
                pass
            elif islem in ["E", "Ç"]:
                break
            else:
                print("Yanlış Seçim")


app = App()
app.init_app()
