#!/bin/python3.9
"""Alist comprehension consists of brackets containing an expression followed by a for 
clause, then zero or more for or if clauses.The result will be a new string"""
print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y])

#the above is equivalent to
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))

print(combs)
#if the expression is a tuple e.g the (x, y) it must be paranthesized
vec = [-4, -3, 0, 2, 4]
print("the original list", vec)
#create a new list with values doubled
print([x*2 for x in vec])
#filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
#apply a function to all the elements
print([abs(x) for x in vec])
#call a method on each element
freshfruit = [' banana','   loganberry','passion fruit  ']
print("original", freshfruit)
print([weapon.strip() for weapon in freshfruit])
#create a list of 2-tuples like (number,square)
print([(x, x**2) for x in range(6)])
#the tuple must be paranthesized, otherwise an error is raised
#flatten a list using list comprehension with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
"""List comprehensions can contain complex expressions and nested functions"""
from math import pi
print([str(round(pi, i)) for i in range(1,6)])

#Nested list comprehensions
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

#the following list comprehension will transpose rows and columns
print([[row[i] for row in matrix] for i in range(4)])
#the above example is equivalent to
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

#which in turn is the same as
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

"""in the real world you should prefer buit-in functions to complex flow statements.The zip()
function would do a greate job for this use case"""
print(list(zip(*matrix)))#the asterisk in this case is used to unpack whatever is in matrix

#the del statement
"""there is a way to remove an item from a list given its index instead of its value.the 
del statement.can also be used to remove slices from a list or clear the entire list"""
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a [:]
print(a)