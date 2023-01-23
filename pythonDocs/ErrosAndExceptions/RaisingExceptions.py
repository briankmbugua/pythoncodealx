#!/bin/python3.9
"""the raise statement allows the programmer to force a specified exception to occur """
#example

#raise NameError('HiThere')

"""the sole argumemt to raise indicates the exception to be raised.This must be either an exception
instance or an exception class"""

#raise ValueError #shorthand for 'raiseValueError()

"""if you need to determine whether an exception was raised but don't intend to handle it
a simpler form of the raise statement allows you to re-raise the exception"""

try:
    raise NameError('hey there')
except NameError:
    print('An exception flew by')
    raise #this will cause the NameError('hey there) exception to be handled
          #since the NameError that was raised in the try block was handled by the
          #except block, therefore adding raise at the end raise the same exception again

