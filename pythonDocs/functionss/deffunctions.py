#!/bin/python3.9

#print fibonacci series up to n

def fib(n):
    a,b=0,1
    while a<n:
        print(a, end=' ')
        a, b=b, a+b
    print()

# now call the function we just defined
fib(2000)

"""
the keyword def introduces a function defination. it must be followed by the function name
and the parenthesized list of formal parameters
the statements that form the function must start at the next line and must be idented
The execution of a function introduces a new symbol table used for the local variables of the function
All variable assingments in a function store the value in a local symbol table
Variable references first look in the local symbol table, then in the local symbol table of enclosing functions
then in the global symbol table, and finally in the table of built in names
Thus global variables and variables of enclosing functions cannot be directly assinged a value within
a function althoug they may be referenced
Arguments are passed using call by value
"""
print(fib)

f = fib
f(100)

#it is simpe to write a function that returns a list of numbers of the
#fibonacci series insted of printing it

def fib2(n):
    """return a list containing the fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)

"""
it's possible to define a function with a variable number of arguments
There are three forms that can be used
"""
#Default Arguments Values
#the most useful form is to specify a default value for one or more arguments
#this creates a function that can be called with fewer arguments than it is defined to follow

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in('n','no','nop','nope'):
            return False
        retries = retries - 1        
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)    

#ask_ok('Ok to overwrite the file?',2,'stop guessing and use yes or no')

"""
the in keyword tests whether or not a sequence contains a certain value
"""
#the default values are evaluated at the point of function defination in the defining scope,
#so that
i = 5
def f(arg=i):
    print(arg)
i = 6
f()
"""
the default value is only evaluated once, this makes a difference when the default is a mutable
object such as a list, dictionary or instances of most classes
The function below accumulates the arguments passed to it on subsequent calls
"""
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(3))
print(f(2))

#if you don't want the default values shared between subsequent calls, you can write the function
#like this instead
def g(a, L=0):
    if L is 0:
        L = []
    L.append(a)
    return L
"""print(g(10))
print(g(10))
print(g(10))
"""
#KEYWORD ARGUMENTS
"""
functions can also be called using keyword arguments of the form kwarg=value, for instance the following
function
"""
def parrot(voltage, state='a stiff',action='voom',type="Norwegian Blue"):
    print("-- This parrot wouldn't ", action, end='')
    print("if you put", voltage, "volts through it.")
    print("-- lovely plumage, the", type)
    print("--it's", state,"!")
 
"""
accepts one required argument(voltage) and three optional arguments(state,action and type)
can be called in any of the following ways
"""
#parrot(1000)
#parrot(voltage=1000)
#parrot(voltage=1000000, action='VOOOOOM')
#parrot(action='VOOOOOM', voltage=1000000) 
#parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')

"""
in a function call, keyword arguments must follow positional arguments.
"""
def example_function(positional_arg, keyword_arg=None):
    print(positional_arg, keyword_arg)

example_function(1, keyword_arg=2)
#example_function(keyword_arg=2,1)#this is wrong
#no argument may receive a value more than once

def function(a):
    pass

#function(0, a=0) TypeError: function got multiple values for argument 'a'