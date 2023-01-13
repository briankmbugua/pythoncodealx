#!/bin/python3.9
#if statement
# x = int(input("please enter an interger \n"))
# if x < 0:
#     x = 0
#     print('negative changed to zero')
# elif x == 0:
#     print('zero')
# elif x == 1:
#     print('single')
# else:
#     print('more')

#elif is short of else if

#for statement
""""
Rather than always iterating over an arithmetic progression of numbers, or giving the user
the ability to define both the iteration step and halting condition like c
Python iterates over the items of any sequence(a list or a string), in the order that they appear in
the sequence
"""
#measure some strings
# words = ['cat','window','ship']
# for w in words:
#     print(w, len(w))

"""code that modifies a collection while iterating over the same collection can be tricky
to get right.Instead it is usually more straight foward to loop over a copy of the
or to create a new collection"""

#sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


#braek and continue statements and else clauses on loops
#the break statement like in c breaks out of the innermst enclosing fo or while loop
#else it is executed when the loop terminates throught the exhaution of the iterable(with for)
#or when the condition becomes false(with while), but not when the loop is terminated by a break 
#statement
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             #n//x '//' operator is used for floor division rounds down to the nearest whole number
#             print(n, 'equals', x, '*', n//x) 
#             break
#         else:
#             #loop fell through without finding a factor
#             print(n, 'is a prime numbers')

"""the continue statement continues with the next iteration of the loop"""
# for num in range(2,10):
#     if num % 2 == 0:
#         print('Found an even number', num)
#         continue
#     print('found an odd number' ,num)

#THE pass statement
"""The pass statement does nothing, it can be used when a statement is required
synstantically but the program requires no action"""

# while True:
#     pass

#This is commonly used for creating minimal classes
# class MyEmptyClass:
#     pass
#Match statement
"""a match statement takes an expression and compares its value to succesive patterns given
as one or more case blocks.In python only the first pattern that matches gets executed and it
can also extracr components"""
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"

#note the last block the "variable name" _ acts as a wildcard and never fails to match.
#if no case passes none of the branches is executed
#http_error(500)
