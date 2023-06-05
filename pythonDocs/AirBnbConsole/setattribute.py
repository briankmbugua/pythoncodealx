#!/usr/bin/python3
"""
setattr() function is used to set a value to the object's attribute. It takes three arguments an object, a string, and an arbitrary value, and returns none.It is helpful when we want to add a new attribute to an object and set a value to it
"""
#SYNTAX
"""
setattr(object, name, value)
object - it is an object which allows its attributes to be changed
name - name of the attribute
value - A value set to the attribute

it returns None to the caller function
"""

#EXAMPLE
class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student(102,"Brian")
print(student.id)
print(student.name)

setattr(student, 'email', 'briank@gmail.com')

print(student.email)
