import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class


class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self, id):
        sql = "select * from student where id = %s"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def deleteStudent(self, studentid):
        sql = "delete from student where id = %s"
        value = (studentid,)
        self.cursor.execute(sql,value) 

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi')
        except mysql.connector.Error as err:
            print('hata:', err)

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def getTeacher(self):
        sql = "select * from teacher"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Teacher.CreateTeacher(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def getStudentByClassId(self, classid):
        sql = "select * from student where classid = %s"
        value = (classid,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def addorEditStudent(self, student:Student):
        if student.id == 0:
            self.addStudent(student)
        else:
            self.editStudent(student)

    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(StudentNumber, Name, Surname, Birthdate, Gender, ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender,student.classid)
        self.cursor.execute(sql,value) 

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi')
        except mysql.connector.Error as err:
            print('hata:', err)

    def editStudent(self, student: Student):
        sql = "update student set studentNumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s, classid=%s where id =%s" 
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender,student.classid, student.id)
        self.cursor.execute(sql,value) 

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('hata:', err)

    def getTeacherById(self, id):
        sql = "select * from teacher where id = %s"
        value = (id,)
        self.cursor.execute(sql, value)
        try:
            obj = self.cursor.fetchone()
            return Teacher.CreateTeacher(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def addTeacher(self, teacher: Teacher):
        sql = "INSERT INTO Teacher(branch, Name, Surname, Birthdate, Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (teacher.branch, teacher.name, teacher.surname, teacher.birthdate, teacher.gender)
        self.cursor.execute(sql,value) 

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi')
        except mysql.connector.Error as err:
            print('hata:', err)

    def editTeacher(self, teacher: Teacher):
        sql = "update teacher set branch=%s, name=%s, surname=%s, birthdate=%s, gender=%s where id = %s"
        value = (teacher.branch, teacher.name, teacher.surname, teacher.birthdate, teacher.gender, teacher.id)        
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err:
            print('hata:', err)

db = DbManager()

# student= db.getStudentById(1)
# student[0].name="Mustafa"
# db.addorEditStudent(student[0])   


# student[0].name = "Cansın"
# # db.addStudent(student[0])
# db.editStudent(student[0])

# students = db.getStudentByClassId(1)
# print(students[0].name)
# print(students[4].name)

teacher = db.getTeacherById(1)

# teacher[0].name = "Bugra"
# teacher[0].surname = "Ates"  
# teacher[0].birthdate = "1997-10-10"
# teacher[0].gender = "E"  
# db.addTeacher(teacher[0])

teacher[0].branch = "Bilişim"
db.editTeacher(teacher[0])


