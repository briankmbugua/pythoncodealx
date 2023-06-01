#!/usr/bin/python3

"""
A class method in python is a special type of method that is bound to the class itself, rather than an instance of the class.This means that a classmethod can be called without creating an instance of the class
To define a classmethod in Python, you use the @classmethod decorator.The syntax is as follows

@classmethod
def method_name(cls, *atgs, **kwargs):
    # method body

The cls parameter in the classmethod defination refers to the class itself.This parameter can be used to access class attributes and methods.
"""

#EXAMPLE OF A CLASS METHOD

class Person:
    @classmethod
    def get_name(cls):
        return cls.__name__

print(Person.get_name())

"""
In the above example, we define a classmethod called get_name in the Person class.This method returns the name of the class.We can call the get_name method on Person without creating an instance of the class.

Classmethods are used for operations that do not depend on an instance of a class.For example a class method can be used to initialize a class, or to perform a calculation that needs to be done on all instances of class.
"""

# Example Two of classmethod in Python


class Person:
    _instances = []

    def __init__(self, name):
        self.name = name
        Person._instances.append(self)
    
    @classmethod
    def count_instances(cls):
        return len(Person._instances)

print(Person.count_instances())

brian = Person('brian')
mbugua = Person('Mbugua')

print(Person.count_instances())
    
