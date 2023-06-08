#!/usr/bin/python3
#PROBLEM
"""You need to check the start or end of string for specific text patterns, such as filename extensions, URL schemes, and so on"""
#SOLUTION
"""A simple way to check the beginning or end of a string is to use the str.startswith() or str.endswith() methods"""

filename = "spam.txt"
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
url.startswith('http:')


"""If you need to check against multiple choices, simply provide a tuple of possibilities to startwith() or endswith()"""

import os
filenames = os.listdir('.')
print(filenames)

print([name for name in filenames if name.startswith(('k','s'))])

print(any(name.endswith('.py') for name in filenames))


"""If you happen to have the choices specified in a list or set, just make sure you convert them using tuple() first."""

choices = ['http:', 'ftp:']

url = 'http://www.python.org'

#print(url.startswiht(choices)) #there will be an error here since a tuple is required as input here
print(url.startswith(tuple(choices)))


#DISCUSSION
"""Similar operations as the abov can be performed with slices but are less far elegant, you might also be inclined to use regular expression this works but is often overkill"""

