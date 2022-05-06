class Student:
    count = 0
    def __init__(self):
        Student.count += 1


std1=Student()
print(Student.count)
std2 = Student()
print(Student.count)
