class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    
    def print(self):
        for s in self.students:
            print(s.name + " " + str(s.age))

s1 = Student("kevin", 22)
s2 = Student("peter", 20)

c = Course("cs", 10)
c.add_student(s1)
c.add_student(s2)
c.print()
# print(len(c.students))