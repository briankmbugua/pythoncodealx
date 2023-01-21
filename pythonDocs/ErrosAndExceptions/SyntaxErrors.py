#!/bin/python3.9
#Syntax Errors
"""Syntax errors also known as parsing errors

while True Print('Hello world')
  File "/home/letbmk/Documents/pythonalx/pythonDocs/ErrosAndExceptions/./SyntaxErrors.py", line 4
    while True Print('Hello world')
               ^
SyntaxError: invalid syntax

The error is caused by (or atleast detected at) the token preceding the arroe'^', in the example
the error is detected at the function print(), since a colon (:) is missing before it.
File name and number are printed so you know where to look in case the input came from a
script
"""
#EXCEPTIONS
"""even if a statement is syntatically correct, it may cause an error when an attempt is made to
execute it, errors detected during execution are called exeptions"""

#10 *(1/0) #zero division error
#4 + spam * 3 #spam is not defined NameError
#'2' + 2    #'2' + 2 TypeError: can only concatenate str (not "int") to str TypeError
"""the string printed as the exeption type is the name of the buitin exeption that occured
"""
