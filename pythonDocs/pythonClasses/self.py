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

When an instance of the 'MyClass' is created and the 'my_method() is called on
the instance, the instance ('my_obj') is automatically passed as the first argument ('self')
to the method, allowing the method to acces and modify the properties and state of the instance
"""

#the '__init__' method
"""The '__init__' method is a special method in python classes that is automatically called
when an instance of the class is created.
It is commonly used to set up the initial state of the instance, such as initializing instance
variables

In this case the '__init__' method accepts 'self' and 'value' as parameters and assings
the 'value' passed to the instance variable 'self.value'
When the line 'my_obj = MyClass(5)' is executed, it creates an instance of the 'My_class' and
the '__init__' method is called with 'self' set to the newly created instance and 'value' is
set to 5
"""
