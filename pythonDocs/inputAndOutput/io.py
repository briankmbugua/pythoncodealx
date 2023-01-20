#!/bin/python3.9
#fancier output formatting
#fstrings
"""To use formatted string literals, begin a string with f or F before the opening quatation
mark or tripple quotation mark.You can write a Python expression between '{and}' characters
that can refer to variables or literal values"""

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

#str.format()

"""The str.format() method of string requires more manual effort.You'll still use { and }
to mark where a variable will be substituted and can provide detailed formatting directives,
but you'll also need to provide the information to be formatted"""
yes_votes = 42_572
no_votes = 43_132
percentage = yes_votes/ (yes_votes + no_votes)

print('{:-9} YES votes {:2.5%}'.format(yes_votes, percentage))
#{:d} - integer, {:f} - floating point number, {:2f} - floating point number with 2 decimal places
#{:s} - string, {:%} - percentage, {:.2%} - percentage with two decimal places, 
# {:,} - number with comma as the thousands separator, {:>10} - right justified in a field of width of 10
#{:<10} - left justified in a field width 10, {:^10} center justified in a field width 10


"""When you don't need fancier output you can convert any value to string with repr() or str()
functions"""
#str() - human readable output
#repr() for the interpreter

s = 'Hello, world'
print(str(s))#str()
print(repr(s))#repr() output has quotes around it
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '....'
print(s)

#The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
#the argument to repr() may be any python project
argrepr = repr((x, y, ('spam','eggs')))
print(argrepr)

#formatted string literals or f-strings

import math
print(f'the value of pie is aproximately {math.pi:.3f}.')

"""passing an interger after the ':' will cause that field to be a minimum number of characters
wide"""

table = {'Sjoerd':42127, 'Jack':4098,'Dcab':7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

#there can be more formatting with '!a' applies ascii(), '!s' applies str, '!r' applies repr()

animals = 'eels'
print(F'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of animals {animals!r}') #repr() applied using '!r'

#THE STRING format() Method
#str.format()
print("We are the {} who say '{}!'".format('knights', 'Ni'))
"""The brackets and characters are called format fields and are replaced with objects
passed into the str.format() method.A number in the brackets can be used to refer to the 
position of the object passed into str.format() method"""

print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

"""if keyword arguments are used in str.format(), their values are reffered to by using the
the name of the argument"""
print('This {food} is {adjective}'.format(
    food='spam', adjective='absolutely horrible'
))

"""positional and keyword arguments can be arbitrarily combined"""

print('{0}, {1} and {other}'.format('brian','mbugua', other='kinyanjui'))


"""you can reference the values to be formatted by name instead of by position"""
table = {'id': 4127, 'adminNo': 7774, 'age': 26}
print('firstName:{0[adminNo]:d};age:{0[age]:d}'.format(table))
"""this could also be done by passing the table dictionary as keyword arguments with
** notation"""
table = {'id': 4127, 'adminNo': 7774, 'age': 26}
print('firstName:{adminNo:d};age:{age:d}'.format(**table))

#another example using for in range()
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


#manual string formatting
for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end= ' ')
    print(repr(x*x*x).rjust(4))
#in the output the space in between the columns is added by the way print() works
#it adds spaces between it's arguments
#str.rjust() right justifies a string in a field of a given width by padding it with spaces on
#the left, str.ljust() works the same but left justified, str.center() works the same but centers

for x in range(1,11):
    print(repr(x).center(0), repr(x*x).center(0), end= ' ')
    print(repr(x*x*x).center(0))

#str.zfill() it pads numeric string on the left with zeros
print('12'.zfill(5))

#old string formatting
""" The % operator(modulo) can also be used for string formatting, Given 'string' % values 
instances of % in string are replaced with zero or more elements of values, this operation is
commonly known as string interpolation, This is more like printf() from c style formatting"""

