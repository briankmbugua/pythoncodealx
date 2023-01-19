#!/bin/python3.9

#Built-in -- contains built in functions and expection names, 
#            it is created when the python interpreter starts up
#            and is never deleted
#Global(in a module) -- Contains global names defined in a module
#                       it is created when the module defination
#                       is read in and is deleted when the interpreter quits
#Local(in a function) -- Contains local names defined in a function,
#                        it is created when the function is called and deleted
#                        when the function returns or an exception is raised
#Atrribute of an object -- contains attributes of an object, it is created when
#                          the object is created and it is destroyed when the object
#                          is deleted or garbage collected                           


#Global namespace
x = 5
def example():
    #Local namespace
    x = 10
    print("from inside the function",x)

example()

print("from outside the function", x)

#you can also use the keyword 'global' to reference the global namespace within a function

y = 5

def example2():
    global y
    y = 10
    print("inside the function y is",y)

print("before calling the function y is",y)
example2()
print("after calling the function which uses global keyword y is", y)
print("the value of the global y has been changed inside the function y is", y)

#the 'nonlocal' keyword can beused to reference a variable in an enclosing(but not global)
#namespace
#both inner and outer v will be 20
def outer():
    v = 10
    def inner():
        nonlocal v
        v = 20
        print("Inner:", v)
    inner()
    print("Outer:", v)

outer()
#same functions without the nonlocal keyword the inner v will be 20, and outer v will 10
def outer():
    v = 10
    def inner():
        v = 20
        print("Inner:", v)
    inner()
    print("Outer:", v)

outer()
