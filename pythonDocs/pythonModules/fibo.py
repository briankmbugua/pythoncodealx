#!/bin/python3.9
#Fibonacci numbers module
def fib(n):  #write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        #print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return print(result)

def fib3(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

def fib4(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return print(result)
