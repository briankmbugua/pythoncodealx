"""python has a way to put definations in a file and use them in a script or in an interactive instnce
of the interpreter.Such a file is called a MODULE definations from a module can be imported into
other modules or into the main module
A module is a file containing Python definations and statements"""
#Fibonacci numbers module
def fib(n):  #write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

#use inside the python interpreter
#commands
#~(main):  python3.9
#>>>import modules
#>>>modules.fib(10) 1 1 2 3 5 8
#>>>modules.fib2(10) [0, 1, 1, 2, 3, 5, 8]
"""if you intend to use a function often you can assgn it to a local name"""
#>>>fib = modules.fib
#>>>fib(10) 1 1 2 3 5 8

#MORE ON MODULES
"""A module can contain executable statements as well as function definations.These statements
are intended to initialize the module.They are """

#More on modules
"""a module can contain exexcutable statements as well as function definations.These statements
are meant to initialize the module.They are executed only the first time the module name is
encountered in an import statement
Each module has it's own namespace, which is used as the global namespace by all functions
defined in the module
Modules can impoer other modules, it customary not required to place all import statements
at the beginning of a module,The imported modules if placed at the top level of a module
(outside any functions or classes) are added to the modules global namespace"""

#importing names from a module directly into the importing module's namespace
"""
from fibo import fib, fib2 ---> 
fib(500)
This does not introduce the module name from which the imports are taken in the local namespace
(so in the example fibo is not defined)

Import all names that a module defines

from fibo import *
fib(500)
This imports all names expect those beginning with an underscore(_) this facility is
not often used since it introduces an unknown set of names into the interpreter

import fibo as fib
fib.fib(500)
if the module name is followed by as, then the name following 'as' is bound directly to
imported module
I can also be used when utilising from with similar effects
from fibo import fib as fibonacci
fibonacci(500)
"""



