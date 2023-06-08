#!/usr/bin/python3
from models.engine import storage
from models.base_model import BaseModel

# all_objs = storage.all()

# print("__ Reloaded objects")

# for obj_id in all_objs.keys():
#     obj = all_objs[obj_id]
#     print(obj)

# print("-- Create a new object --")
# my_model = BaseModel()
# my_model.name = "My_Second_Model"
# my_model.my_number = 90
# my_model.save()
# print(my_model)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# newPerson = Person('brian', 100)

# print(newPerson)

# newPersonTwo = eval('Person')('brian', 10)

# print(newPersonTwo.name)


newPerson = Person('brian', 100)

print(newPerson.name)
print(newPerson.age)

newPersonTwo = eval('Person')('brian',100)

print(eval('Person'))
print(Person)

print(newPersonTwo.name)
print(newPersonTwo.age)
