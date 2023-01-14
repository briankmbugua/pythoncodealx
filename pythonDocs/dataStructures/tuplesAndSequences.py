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
"""tuples are immutable and usually contain a heterogeneous sequence of elements that are
accessed via unpacking or indexing or by attributein the case of namedtuples while lists are
mutable and their elements are usually homgeneous and are accesed by iterating over the list"""
"""A SPECIAL PROBLEM is the construction of tuples containing 0 or 1 items the syntax has some 
extra quirks to accomodate these.Empty tuples are constructed by an empty pair of parentheses,
a tuple with one item is constructed by following a value with a comma"""
empty = ()
singleton = 'hello',#must have a comma to have just one value
len(empty)
len(singleton)
print(singleton)
#tuple packing
t = 1,2,3,'hello'
print(t) #(1, 2, 3, 'hello')
x,y,z,w = t # this is called sequence upacking
print(x)#1
print(y)#2
print(z)#3
print(w)#'hello'