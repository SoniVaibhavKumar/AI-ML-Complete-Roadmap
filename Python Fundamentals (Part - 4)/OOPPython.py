# Class : Blueprint of an object
# Object : Instance of class

class Student:
    subject = "Python"
    college = "ABC"
    year = "4th year"

stu1 = Student()
stu2 = Student()
print(stu1.subject, stu1.college, stu1.year)
print(stu2.subject, stu2.college, stu2.year)

class Students:
    def __init__(self, names, cgpas):
        self.names = names
        self.cgpas = cgpas
stud1 = Students("Rahul", 9.0)
stud2 = Students("Urvashi", 9.0)
stud3 = Students("Shradha", 9.0)
print(stud1.cgpas)
print(stud2.names)
print(stud3.names)