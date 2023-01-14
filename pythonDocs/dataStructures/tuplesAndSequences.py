#!/bin/python3.9
"""lists and strings ahve many common properties such as indexing and slicing operations
There are two examples of sequence data types(list,tuple,range)"""
"""a tuple consists of a number of values separated by commas"""

t = 12345,54321,'hello!'
print(t[0])
print(t)
#tuples may be nested
u = t, (1,2,3,4,5)
print(u)
#tuples are immutable
#t[0] = 88888 TypeError: 'tuple' object does not support item assignment
#but the can contain mutable objects
v = ([1,2,3],[3,2,1])
print(v)