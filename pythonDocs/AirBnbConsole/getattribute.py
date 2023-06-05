#!/usr/bin/python3
"""getattr() function is used to get the value of an obecs attribute and if no attribute of that object is found, default value is returned"""
#SYNTAX
"""getattr(object_name, attribute_name[, default_value])"""
#EXAMPLE

class Student:
    student_id = ""
    student_name = ""
    # intial constructor to set the values
    def __init__(self):
        self.student_id = "101"
        self.student_name = "Adam Lam"

student = Student()

# get attribute values by using getattr() function
print('\ngetattr : name of the student is =', getattr(student, "student_name",))

#can also be accessed like this
print('traditional: name of the student is =', student.student_name)
# USING getattr default option

print('Using default value: Cgpa of the student is =',getattr(student, "student_cgpa", 3.00))

# WITHOUT USING THE DAFAULT VALUE
try:
    print('Without default value: cgpa of the student is = ',getattr(student,"student_cgpa"))
except AttributeError:
    print("Attribute is not found:(") # AttributeError is raised when the default value is not provided while calling getattr() function

# Reason for using Python getattr() function
"""The main reason to use python getattr() is that we can get the value by using the name of the attribute as a String.So you can manually input the attribute name in your program from console.Again if an attribute is not found you can set some default value which enables us to complete some of our incomplete data"""