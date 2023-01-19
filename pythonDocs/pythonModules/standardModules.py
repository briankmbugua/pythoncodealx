#!/bin/python3.9

"""Python comes with a library of standard modules"""
#sys modules is built into every Python interpreter.The variables sys.ps1 and sys.Ps2
#define the strings used as the primary and the secondary outputs

import sys, fibo
#print(sys.path)

#dir() Function
"""The built-in function dir() is used to find out which names a module defines.
It returns a sorted list of strings"""
print("the dir() function")
#sprint(dir(fibo))
#print(dir(sys))
#without arguments dir() list the names you have defined currently
testName = [1,2,3,4]
fib = fibo.fib
#print(dir())
"""dir() does not list the names of buit-in functions and variables.If you want a list of 
those, they are defined in the standard module builtins"""
import builtins
print(dir(builtins.tuple.index))
