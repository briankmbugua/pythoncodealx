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
#identifiers with the form _spam(at least two leading underscores, at most one trailling
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
                      #this allows it to be called using either names
                      #__update or update

class MappingSubclass(Mapping):
    def update(self, keys, values):#this is method overriding
#this means when the 'update' method is called on an instance of the MappingSubclass
#the implementation defined in the subclass will be executed rather than the one in the parent class
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

#example 2

class Animal:
    def __init__(self, type,animal):
        self.animal = animal
        self.__name = type
    def  changeType(self,type):
        self.__name = type
    def whatIsThis():
        return 

# class Dog(Animal):

dog = Animal('wild','animal')
print(dog.animal)
print(f"before using changeType() method, {dog._Animal__name}")
dog.changeType("domestic")
print(f"After using changeType() method, {dog._Animal__name}")

#print(dog._Animal__name) #Using name mangling to access a private variable
                         #but this should not be done as per python community guidline

#creating a subclass of Animal

class Bird(Animal):
    def __init__(self,name):
        super().__init__(type,'bird')
        self.name = name
    def changeType(self, type):
        self.name = type

eagle = Bird('airboone')
print(eagle.name)
print(eagle.changeType('Ground')) #method overiding the changeType
print(eagle.name)
print(eagle.animal)#without calling super you cannot acces animal from
                   #the child class
                   #this shows that the 'child' class can access the 'value'
                   #variable from its parent class, but it does not inherit it
                   #automatically, instead it must call the parent class '__init__' 
                   #method in order to access the variable

