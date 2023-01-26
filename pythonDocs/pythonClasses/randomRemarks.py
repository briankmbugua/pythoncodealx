#!/bin/python3.9
"""If the same attribute name occurs in both an instance and in a class, then attribute
lookup prioritizes the instance
"""


class Warehouse:
    purpose = 'storage'  # class variable
    region = 'west'


w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)

# 1.Data attributes(also known as instance variables) can be referenced by methods
#  and clients of an object in python
"""
In Python, data attributes (also known as instance variables) can be accessed and 
modified by methods and clients (i.e. other objects or code) 
that have access to the object. This can be done using the dot notation, 
such as "object.attribute" to access the attribute, 
and "object.attribute = value" to set the attribute to a new value. 
Data attributes are typically used to store the state of an object.
"""
# 2.Classes do not enforce data hiding and its based on convention

"""
 Python does not have a built-in mechanism for enforcing data hiding in classes. 
 Data hiding is a concept in object-oriented programming 
 where the internal state and implementation of an object are kept hidden or 
 encapsulated from the outside world. Instead, it relies on naming 
 conventions to indicate which attributes and methods should 
 be considered part of the class's public interface and 
 which should be considered private. By convention, attributes and methods 
 with names starting with an underscore (_) are considered private 
 and should not be accessed or modified directly by clients. 
 However, this is just a convention and there is nothing 
 stopping clients from accessing or modifying these attributes if they choose to do so.
"""
# 3.Clients should use data attributes with care to avoid messing up invariants maintained
# by methods
"""
 If an object has certain invariants (i.e. conditions that must always be true) that are maintained by its methods, it is important for clients to use the object's data attributes with care to ensure that these invariants are not violated. For example, if an object has a "balance" attribute that represents the current balance of an account, and a "withdraw" method that subtracts a certain amount from the balance, it is important for clients to use the "withdraw" method rather than directly modifying the "balance" attribute, to ensure that the balance does not become negative.

Clients should also be aware of the constraints and invariants of the object, and should not use data attributes in a way that would violate them. For example, an object might have an attribute that should only be set to a positive number, and clients should be careful not to set that attribute to a negative number.

Additionally, it is best practice that the class should have methods to access and modify the data attributes, instead of accessing them directly. This allows the class to keep the consistency of its internal state and also provide a way to validate the input before actual modification.
"""
# 4.There is no shorthand for referencing data attributes from within methods, this
# increases redability
"""In Python, there is no shorthand for referencing data attributes from within methods. When accessing or modifying an object's data attributes from within its methods, the full notation "self.attribute" must be used. This is to clearly indicate that the attribute being accessed or modified is a data attribute of the object, and not a local variable or a parameter of the method.

This approach increases the readability of the code, as it makes it clear that the attribute being accessed or modified is part of the object's state, and it also makes it easy to distinguish between data attributes and local variables or parameters. It also makes it clear which object the attribute belongs to, and avoid confusion between multiple instances of the same class.

Additionally, in large and complex projects, the use of the full notation self.attribute instead of a shorthand notation can make it easier to track down bugs and understand the flow of data within the program."""
# 5.The first argument of a method is called self, but it has no special meaning in Pyhton
# and is just a convention
"""In Python, the first argument of a method is commonly named "self" as a convention, but it has no special meaning in the language itself. The name "self" is used to refer to the instance of the class that the method is being called on. The use of "self" as the name of the first argument is a convention that is widely used in the Python community, but it is not a language requirement or a keyword.

It is important to note that in Python, "self" is just a variable like any other. It is not a keyword and has no special meaning. The only special thing about it is that it is passed to the method as the first argument when the method is called on an instance.

It is also possible to use other names for the first argument, such as "this" or "cls", but using "self" is the most common and recommended practice. This makes it easier for other developers to understand the code and follow the conventions of the Python community."""
# 6.Any function object that is a class attribute defines a method for instances of that
# class, and function defination does not have to be textually enclosed in the class defination
"""In Python, any function object that is a class attribute defines a method for instances of that class.

When a function is assigned as a class attribute, it can be called on instances of the class as a method. This is known as "binding" the function to the class, and it is done by passing the instance as the first argument to the function, also known as the "self" argument.

It is also true that the function definition does not have to be textually enclosed in the class definition. You can define a function outside of the class definition and then assign it as a class attribute.

This allows for a more flexible and modular organization of code, and also allows for the reuse of functions across multiple classes.

It's also worth noting that you can use the @decorator syntax to define the methods of a class, this way the function definition is not within the class definition but it is still a method of the class."""

#above explained in code
class MyClass:
    def __init__(self):
        self._data = 0  # data attribute, conventionally indicated with a single leading underscore
        
    def my_method(self):   # method, which has access to the data attribute
        self._data += 1
        return self._data
        
    def _my_private_method(self):  # private method, conventionally indicated with a double leading underscore
        self._data -= 1
        return self._data
        
    def my_function(self, value):  # function that can be used as a method
        self._data += value
        return self._data

def my_function2(self, value): # function that can be assigned as a method
    self._data += value
    return self._data

MyClass.my_function2 = my_function2
        
# create an instance of MyClass
my_object = MyClass()

# access the data attribute
print(my_object._data)  # 0

# use the my_method method to increment the data attribute
print(my_object.my_method())  # 1

# use the my_function method to increment the data attribute
print(my_object.my_function(5))  # 6

# use the my_function2 method to increment the data attribute
print(my_object.my_function2(5))  # 11

# trying to access the private method raise an error 
#print(my_object._my_private_method()) # will raise an error

#xample2


"""Any function object that is a class attribute defines a method for instances of that class
It is not necessary that the function defination is textually enclosed in the classs defination
Assingning a function object to a local variable is also okay"""

def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'Hello world'
    h = g



"""
Now f, g and h are all attributes of class C that refer to function objects, and consequently
they are all methods of instances of C   h being excatly equivalent to g.NB THIS ONLY SERVES
TO CONFUSE THE READER OF A PROGRAM
"""


#Methods may call other methods by using method attributes of the self argument
y = 20
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
        print("the value of the global y",y)#methods in python can reference global scope
                                            #just like normal functions
        return self.data

    def addTwice(self, x):
        self.add(x)
        self.add(x)
bag = Bag()
print(bag.add(50))

#1.methods in python can reference global scope
#just like normal functions
#2.The global scope associated with a method is the module containing its defination
#if you import the module in another file, to use variables in the imported module
#you have to go through the methods and function defined in that imported module 
#A class does not exist in isolation, it is defined inside a module and can acces the gobal
#scope of that module but it is not considered to be part of the global scope

class Myclass:
    pass

obj = MyClass()
print(obj.__class__)  #<class '__main__.MyClass'>
#Here 'obj' is an instance of 'MyClass' and the '__class__'
#and the attribute of 'obj' is a reference to class object 'MyClass'
#you can use this attribute to check the class of an object, or to check if an object
#is an instance of a particular class
print(obj.__class__)

