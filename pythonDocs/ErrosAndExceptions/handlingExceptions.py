#!/bin/python3.9
"""it is possible to write programs that handle selected exceptions"""
#example
while True:
    try:
        x = int(input('please enter a number'))
        break
    except ValueError:
        print("OOPS That was no valid number. Try again...")

"""the try statement works as follows
. first, the try clause statements between try and except is executed.
. if no exception occurs, the exept clause is skipped and the execution of the try statement
is finished
. if an exception occurs during the execution of the try clause, the rest of the clause is
skipped, Then if its type matches the exception named after except keyword, the except clause
is executed, and the execution continue after the try/except block
. if an exception occurs which does not match the exception named in the except clause, it is 
passwd on to outer try statements; if no handler is found it is an unhandled exception and
execution stops with a message"""


print('MULTIPLE EXCEPT CLAUSES')
"""A try clause may have more than one except clause, to specify handlers for different
exceptions"""
try:
    pass
    #code that may raise an exception
except RuntimeError:
    pass
    #code to handle ExceptionType1
except TypeError:
    pass
    #code to handle ExceptionType2


try:
    x = 5 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')
except TypeError:
    print('Invalid operation')


"""An except clause may name multiple exceptions as a parenthesized tuple"""

try:
    pass
except(RuntimeError,TypeError, NameError):
    pass


try:
    x = int('abc')
except(ValueError, TypeError):
    print('invalid input') #you will get this since abc is not an int

"""A try-except block with a single except clause without an exception type
the except clause catches any exception raised in the try block amd prints a message"""
print('AN except clause with no exception type')

try:
    x = 5 / 0 #will raise ZeroDivisionError
    y = 'abc' + 5 #will raise TypeError
except:#will catch any exception raised since except has no exception type
    print('An error occured')

"""The except clause may specify a variable after the exception name.The variable is bound
to the exception instance which typically has an args attribute that stores the arguments
that were passed to the exception when it was raised.
By binding the exception to a variable in the except clause, you can acces these arguments
and use them to provide more detailed information about the exception to the user for
debugging purposes"""

#example
print("A TRY EXCEPT BLOCK THAT USES A VARIABLE")

try:
    x = 1 / 0 #will raise a ZeroDivisionError
except ZeroDivisionError as e:#the except block uses the as keyword to bind the exception instance
                              #to variable e
    print("caught an exception", e)
    print("Arguments", e.args)

"""It is also possible to handle multiple exception types in the same except block """
print("A TRY EXCEPT BLOCK THAT USES A VARIABLE WITH MULTIPLE EXCEPTION TYPES")
try:
    x = 1 / 0
except(ZeroDivisionError, TypeError) as e:
    print("Caught an exception", e)
    print("Arguments:", e.args)



"""Built in exception types define __str__() to print all the arguments with explicitly
accessing .args
The expection's __str__() output is printed as the last part('detail') of the message of
unhandled exceptions"""
try:
    raise Exception('spam','eggs')
except Exception as inst:
    print(type(inst)) #the exception instance
    print("arguments stored in .args",inst.args)
    print(inst) # __str__ allows args to be printed directly
                #but may be overriden in exception subclasses
    x, y = inst.args #unpack args
    print('x=', x)
    print('y =', y)




