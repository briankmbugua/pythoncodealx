#!/bin/python3.9
#Fibonacci numbers module
def fib(n):  #write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        #print()

fib(30)

"""When you run a Python module with
python fibo2.py <arguments>
the code in the module will be executed, just as if you imported it, but with the __name__
set to '__main__' That means by adding the following code at the end of your module:
"""

if __name__=="__main__":
    import sys
    fib(int(sys.argv[1]))

"""you can make the file usable as a script as well as an imported module, because the code
that passes the command line only runs if the module is executed as the "main" file"""
#this will work
# $ python3.9 fibo2.py 50
# 0 1 1 2 3 5 8 13 21 34
"""if the module is imported the code does not run"""
#>>>import fibo2
#>>>