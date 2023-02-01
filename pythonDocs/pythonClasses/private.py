#!/usr/bin/python3.9

class Example:
    def __init__(self):
        self.__secret = 42
    def get_secret(self):
        return self.__secret

example = Example()
print(example._Example__secret)

class Person:
    def __init__(self):
        self.__name = "brian"
    def get_name(self):
        return self.__name

person = Person()
print(person._Person__name)

# class Animal:
#     def __init__(self):
#         self.name = "Cow"
#     def get_name(self):
#         return self.name
# cow = Animal()
# print(Animal.name) #this gives an error of animal has no attribute name
                   #but it can be accesed using name mangling by prefixing the class name and
                   #double underscores to the variable name
class Animal:
    def __init__(self):
        self.__name = "Cow"
    def get_name(self):
        return self.__name
cow = Animal()
print(cow._Animal__name)
print(cow.get_name())