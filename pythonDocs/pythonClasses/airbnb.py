#!/usr/bin/python3.9

class Student:
    #class variables
    """Student Class"""
    sex = "male"

    def __init__(self,course,grade):
        self.course = course
        self.grade = grade
    def getDetails(self):
        print(f"sex is {self.sex},\n course is {self.course}, grade is {self.grade}")
student1 = Student("alxse",100)
student2 = Student("alxAwss", 90)

student1.getDetails()
student2.getDetails()

#doc
print(Student.__doc__)
print(Student.__class__)
print(Student.__repr__)
print(Student.__init__)
print(Student.__itemsize__)

    


