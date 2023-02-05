#!/bin/python3.9
#multiple inheritance
#1.Allows a class to inherit attributes and behaviours from multiple parent classes
# Achieved by defining a class with multiple base classes separated by commas in the class defination
# Child class has access to the attributes and bahaviours defined in all its classes
# If two parent classes define the same attribute or method, the child class will inherit only the first one defined, leading to ambiguity
# Method resolution order algorithm determines which parent class's attributes should be used in case of confilicts


# class Parent1:
#     def __init__(self):
#         self.attribute1 = "Parent1 attribute"
#     def method1(self):
#         print("Method 1 from Parent1")

# class Parent2:
#     def __init__(self):
#         self.attribute2 = "Parent2 attribute"
#     def method2(self):
#         print("Method2 from parent2")

# class Child(Parent1,Parent2):
#     pass

# child = Child()
# print(child.attribute1)
# print(child.attribute2)
# child.method1()
# child.method2()

class Parent1:
    def __init__(self):
        self.attribute1 = "Parent1 attribute"

    def method1(self):
        print("Method 1 from Parent1")

class Parent2:
    def __init__(self):
        self.attribute2 = "Parent2 attribute"

    def method2(self):
        print("Method 2 from Parent2")

class Child(Parent1, Parent2):
    def __init__(self):
        Parent2.__init__(self)

child = Child()
print(child.attribute1)
print(child.attribute2) 
child.method1() # Output: "Method 1 from Parent1"
child.method2() # Output: "Method 2 from Parent2"
