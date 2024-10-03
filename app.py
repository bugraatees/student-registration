from dbmanager import DbManager
import datetime
from Student import Student
from Teacher import Teacher

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*******\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Öğretmen Listesi\n7-Çıkış(E/H)"
        while True:
            print(msg)
            islem = input("Seçim : ")
            if islem == '1' :
                self.displayStudents()
            elif islem == '2':
                self.addStudent()
            elif islem == '3':
                self.editStudent()
            elif islem == '4':
                self.deleteStudent()
            elif islem == '5':
                self.addTeacher()
            elif islem == '6':
                self.displayTeachers()
            elif islem == 'E' or islem == 'H':
                break
            else:
                print('Yanlış Seçim Yapılmıştır')

    def addTeacher(self):
        self.displayTeacher()

        branch = input('Bölüm : ')
        name = input ('ad : ')
        surname =input ('soyad : ')
        year = int(input ('yıl : '))
        month = int(input ('ay : '))
        day = int(input ('gün : '))
        birthdate = datetime.date(year,month,day)
        gender = input('cinsiyet(E/K)')

        teacher = Teacher(None,branch, name,surname,birthdate,gender)
        self.db.addTeacher(teacher)


    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Ögrenci Id : '))

        self.db.deleteStudent(studentid)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Ögrenci Id : '))

        student = self.db.getStudentById(studentid)

        student[0].name = input('name : ') or student[0].name
        student[0].surname = input('surname :') or student[0].surname
        student[0].gender = input('cinsiyet (E/K) :') or student[0].gender
        student[0].classid = input('Sınıf :') or student[0].classid
        
        year = input("Yıl :") or student[0].birthdate.year
        month = input("Ay :") or student[0].birthdate.month
        day = input("Gün :") or student[0].birthdate.day

        student[0].birthdate = datetime.date(year,month,day)
        self.db.editStudent(student[0])


    def addStudent(self):
        self.displayClasses()

        classid = int(input('Hangi Sınıf : '))
        number = input('numara : ')
        name = input ('ad : ')
        surname =input ('soyad : ')
        year = int(input ('yıl : '))
        month = int(input ('ay : '))
        day = int(input ('gün : '))
        birthdate = datetime.date(year,month,day)
        gender = input('cinsiyet(E/K)')

        student = Student(None,number, name,surname,birthdate,gender,classid)
        self.db.addStudent(student)

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}: {c.name}')

    def displayTeacher(self):
        teacheres = self.db.getTeacher()
        for c in teacheres:
            print(f'{c.id}: {c.name}')

    def displayStudents(self):
        self.displayClasses()
        classid = int(input('Hangi Sınıf : '))

        students = self.db.getStudentByClassId(classid)
        print("Öğrenci Listesi")
        for std in students:
            print(f'{std.id}--{std.name} {std.surname}')

        return classid
    
    def displayTeachers(self):
        self.displayTeacher()
        id = int(input('Hangi bölüm : '))

        teachers = self.db.getTeacherById(id)
        print("Öğretmen Listesi")
        for tch in teachers:
            print(f'{tch.id}--{tch.name} {tch.surname} {tch.branch}')

app = App()
app.initApp()


