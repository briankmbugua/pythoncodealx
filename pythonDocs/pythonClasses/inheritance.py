#!/bin/python3.9

#syntax for a derived class defination

#class DerivedClassName(BaseClassName):
    #<statement-1>
    #.
    #.
    #.
    #<statement-2>
"""The name BaseClassName must be defined in a scope containing the derived class defination
In place of a base class name, other expressions are also allowed
This can be used when the base class is defined in another module
"""

#class DerivedClassName(modulename.BaseClassName):


#1.Execution of a derived class proceeds the same as for a base class, with base class being
#remembered when the class object is constructed
#2.Attribute references are resolved by searching the class and its base classes recursively
#3.Instantiation of derived classes is the same as for base classes.
#4.Method references are resolved by searching the corresponding class attribute and its base
#classes recursively
#Derived classes can overide methods of their base classes.
#5.To call the base class method directly, use BaseClassName.methodname(self, arguments),
#this only works if the base class is accesible as BaseClassName in the global scope

#PYTHON HAS TWO BUILT-IN FUNCTIONS THAT WORK WITH INHERITANCE
#1.isinstance() to check an instances's type, isinstance(obj, int) will be True only if
# obj.__class__ is int or some class derived from int
#2.issubclass() to check class inheritance, issubclass(bool, int) is True since bool is a
#subclass of int.However, issubclass(float, int) is False since float is not a subclass of int

print("is bool a subclass of int",issubclass(bool, int))
print("is float a subclass of int",issubclass(float, int))

#Multiple inheritance

#1.Pyhton supports multiple inheritance, where a class can have multiple base classes
#2.The search for attributes inherited from parent classes is done in a depth-first,
#left-to-right order
#3.The method resolution order changes dynamically to support cooperative calls to super(),This
#approach is known as call-next-method and is more powerful than the super call in single
#inherited languages
#4.Dynamic ordering is necessary to handle diamond relationships where a parent class can be
#accessed throught multiple paths, the algorithm linearizes the search order in a way that prevents
#left-to-right ordering, calls each parent only once, and is monotonic
class   Base1:
    pass

class Base2:
    pass

class Base3:
    pass

#A python class with multiple bases looks like this
class DerivedClassName(Base1, Base2, Base3):
    #<statement-1>
    pass
    #<stament-N>

#private variables
#'PRIVATE' instance variables that cannot be accesed except from inside an object don't exist
#in python, however there is a convention followed by most python code,A name prefixed with an
#_underscore(eg _spam) should be treated as the non public part of the API whether it's a function
#a method or a data member

#NAME MANGLING
#this is a mechanism to support class-private members in python
#identifiers with the forn _spam(at least two leading underscores, at most one trailling
# underscore) are replaced with _classname_spam, where class name is the current class name
#with leading underscores stripped
#Mangling is done within the defination of a class and is used to avoid name clashes with names
#defined by subclasses
#The mangling is done textually, regardless of the syntatic position of the identifier

#Name mangling is helpful for letting subclasses overide methods without breaking intraclass
#method calls

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    __update = update # private copy of original update() method

class MappingSubclass(Mapping):
    def update(self, keys, values):
        #provides new signature for upadate()
        #but does not break the __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

print(Mapping)
print(MappingSubclass)

print(issubclass(MappingSubclass, Mapping)) #true

obj = Mapping([1,2,3])
print(obj.items_list)
print(obj.update([3,4,5]))
print(obj.items_list)



