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

