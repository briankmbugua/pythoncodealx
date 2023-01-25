#!/bin/python3.9
"""instance variables are data unique to each instance and class variables
are attributes and methods shared by all instances of the class"""

"""if you want to add tricks list it should not be a class variable since it will be shared
by all dogs and you want it to be unique tricks list for each dog
It should be an instance variable to have unique tricks for each dog"""
class Dog:
    kind = 'canine' #class variable shared by all instances
    #tricks = [] mistaken use of a class variable this will be shared by all dogs
    def __init__(self, name):
        self.name = name #instance variable unique to each instance
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

print(d.kind) # shared by all dogs
print(e.kind) # shared by all dogs
print(d.name) #unique to d
print(e.name) #unique to e
print(d.tricks)
print(e.tricks)


