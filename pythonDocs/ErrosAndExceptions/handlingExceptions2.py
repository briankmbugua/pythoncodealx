#!/bin/python3.9
"""The most common pattern for handling Exception is to print or log the exception and then
re-raise it(allowing a caller to handle the exception as well)"""
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('Os error', err)
except ValueError:
    print("Could not convert data to an interger.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

"""The try...except statement has an optional else clause, which, when present, must follow
all except clause.It is useful for code that must be executed if the try clause does not
raise an exception"""
#optional else statement in try..except clause
try:
    x = int(input("Enter a number"))
    result = 1/x
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("The result is", result)

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

"""Exception handlers do not only handle only exceptions that occur immediately in the try
clause, but also those that occur inside functions that are called(even indirectly) in
the try clause"""


def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)



