#!/bin/python3.9
"""if an unhandled exception occurs inside an except section, it will have the exception being
handled attached to it and include in the error message
"""

# try:
#     open('database.sqlite')
# except OSError:
#     raise RuntimeError('unable to handle error')

"""to indicate that an exception is a direct consequence of another, the raise statement
allows an option from clause
"""

#raise RuntimeError from exc
#exc must be an exception instance or none
#this can be useful when you are transforming exceptions

# def func():
#     raise ConnectionError

# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc

# """it allows disabling automatic exception chaining from None idiom"""
# #User-Defined Exceptions
# """Programs may name their own exceptions by creating new exception class
# Exceptions should typically be derived from the Exception class, either directly or indectly
# """

# #Defining clean-up Actions
# """The try statement has another optional clause which is intended to define clean-up
# actions that must be executed under all circumstances"""

# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world')

"""if a finally clause is present, the finally clause will execute as the last task before the
try statement completes. The finally clause runs whether or not the try statement produces
an exception.
"""
#More complex cases when an exception occurs
"""1.if an exception occurs during execution of the try clause, the exception may be handled
by an except clause, if the exception is not handled by an except clause, the exception is
re-raised after the finally clause has been executed
2.An exception could occur during execution of an except or else clause, Again the exception
is re-raised after the finally clause has been executed
3.if the finally clause executes a break, continue or return statement, the exceptions are not
re-raised
4.if the try clause executes a break, continue or return statement, the finally clause will
execute just prior to break,continue or return statement execution
5.if a finally clause has a return statement, the returned value will be the one from the finally
clause's return statement, not the value from the try clause's return statement
"""

#example
def bool_return():
    try:
        return True
    finally:
        print('inside finally')
        return False
print(bool_return())
#example2
print('#exampl2')
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is', result)
    finally:
        print('executing finally clause')

divide('w','z') #when you divide two strings the exception raised is not handled by 
                #the except clause and therefore re raised after the finally clause has been
                #executed, so finally is executed in any event

"""In real world applications the finally clause is useful for releasing external resources
such as file or network connections regardless of whether the use of the resources was successful"""

#Predefined Clean-up Actions


