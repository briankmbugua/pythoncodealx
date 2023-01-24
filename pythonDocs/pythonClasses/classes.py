#!/bin/python3.9
"""classes introduce a little bit of new syntax, three new object types, and some new
semantics
"""
#CLASS DEFINATION SYNTAX
#THE SIMPLEST FORM OF CLASS DEFIANTION LOOKS LIKE THIS
class ClassName:
    #<statemnent-1>
    pass

    #<statment-N>

"""
1.Class definations, like function definations, must be executed before they take effect
2.The statements inside a class defination are usually function definations, but other statements
are allowed
3.A new namespace is created when a class defination is entered, and is used as the local namespace
4.function definations bind the name of the new function in the new namespace
5.when a class defination is left normally, a class object is created which is a wrapper around the
contents of the namespace
5.The original local scope is reinstated and the object is bound to the class name given in the
class defination header
"""

#class objects
"""class objects upport two kinds of operations:attribute references and instantiation"""
#1.ATTRIBUTE REFERENCE
"""uses standard syntax used for all attribute references in python
obj.name  Valid attributes are all the names that were in the class's namespace when the
object was created"""
#example

class MyClass:
    """A simple class example"""
    i = 12345

    def f(self):
        return 'Hello world'
x = MyClass()
 #MyClass.i and MyClass.f are valid attribute references returning an interger and a function
 #object, respectively.

""" Class attributes can also be assinged to so you can change the value of MyClass.i by
 assingment
 __doc__ is also a valid attribute, returning the docstring belonging to the class
 in this case 'A simple example class'"""

#2.INSTANTIATION
"""Class instantiation uses function notation, just think of it as a parameterless function
that returns a new instance of the class"""

#assuming the above class
x = MyClass() #creates a new instance of the class and assings this object to the local
              #variable x
print(x.i, x.f())
print(MyClass.f(x))
"""
'x.f' is a method object, it is bound to the instance 'x' of the class 'MyClass'
When you call 'x.f()' python will automatically pass the instance 'x' as the first argument
('self') to the method defined in the 'MyClass'
'Myclass.f' is a function object, it is an unbound method, it is a function that is defined
inside the class 'MyClass'but it is not bound to any instance
When you call 'Myclass.f', you would have to pass an instance as the first argument('self')
yourself in order for the function to be able to access the instance's attributes and methods

In simple words 'x.f()' is equivalent to 'MyClass.f(x)' and both will return hello world

The instance object in this case x is passes as the first argument of the function
"""


"""instantiation operation('calling'a class object) creates an empty object.
Many classes like to create objects with instances customized for a specific inital state
To do this use the special method named __init__
"""
#__init__() method
#a class may define a special method called __init__(), like this

def __init__(self):
    self.data = []

"""the init method may have argument's for greater flexibility, in that case arguments given
to the class instantiation operator '()' are passed on to __init__()"""

#example
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r)
print(x.i)

#instance objects
"""the only operations understood by instance objects are attribute references, there
are two kinds of valid attribute names: data attributes and methods

Data attributes need not to be declared, like local variables they spring into existence when 
they are first assinged to
If x is the instance of MyClass created above, the following piece of code will print
the value 16, without leaving a trace"""

x.counter = 1; #counter has springed to existence after being assinged 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

#method
"""the other kind of instance attribute is a method.A method is a function that belongs
to an object
All attribute of a class that are function objects define corresponding methods of its
instances"""

