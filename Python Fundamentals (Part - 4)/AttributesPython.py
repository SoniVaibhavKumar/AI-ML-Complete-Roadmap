class Student:
    college_name = "ABC College"

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
stu1 = Student("Rahul", 9.0)
print(stu1.name)