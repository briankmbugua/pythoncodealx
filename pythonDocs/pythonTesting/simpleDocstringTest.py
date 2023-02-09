#!/usr/bin/python3.9

#Write aautomated test as part of the documentation of a module
#Tests source code by running examples embedded in the documentation and verifying that they produce the same results

def my_function(a, b):
    """
    >>> my_function(2,3)
    6
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b

#to run the tests, use doctest as the main program via the -m option.
#no output is produced during testing, include the -v to make the test more verbose

#doctest also allows for surrounding text, it looks for lines beginning with the interpreter prompt to find the beginning of a test case, and the case is ended by a blank line or by the next interpreter prompt
#example
print('EXAMPLETWO')
print()
def my_function(a, b):
    """Returns a * b
    Works with numbers:
    >>> my_function(2,3)
    6

    and strings:

    >>> my_function('a', 3)
    'aaa'
    """
    return a * b