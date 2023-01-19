#!/bin/python3.9
from fibo import fib, fib2 #importing names from a module directly into the importing
#module's namespace
print("fib23")
print("fib23")
fib(4)
print("\nfib2")
fib2(10)

import fibo
fibo.fib3(20)
fibo.fib4(20)

#import all names that a module defines
from fibo import *
fib(20)
fib4(20)

#if the module name is followed by as, then the name following as is bound directly to the
#to the imported module
import fibo as fib
fib.fib(90)

#as can also be used when utilising from with similar effects
from fibo import fib as fibonacci
fibonacci(500)


