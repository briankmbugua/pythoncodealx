#!/bin/python3.9
"""in python the term 'self' refers to the instance of an object on which a method is 
being called.
It is the first parameter of any method defined in a class, and is used to reference the 
object's properties and methods
When a method is called on an instance of a class, the instance is automatically passed
as the first argument to the method
This allows the method to access and modify the properties and state of the instance, and
perform actions based on the state
Self can be named anything"""

#example

class MyClass:
    def __init__(self, value):
        self.value = value
    def my_method(self, arg1, arg2):
        # "self" refers to the instance of MyClass
        #on which this method is being called
        result = self.value + arg1 + arg2
        print(result)

# create an instance of MyClass

my_obj = MyClass(5)

my_obj.my_method(2, 3)

"""In this example, the 'MyClass' has a constructor method '__init__'
which accepts self and a value as the parameter and assings the value
passed to the instance variable 'value'

The 'my_method' method accepts self,arg1,arg2 as parameter and uses and
uses 'self.value' which is the instance variable to perform some operation
and print the result
"""
