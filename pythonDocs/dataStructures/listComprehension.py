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
#if the expression is a tuplee.g the (x, y) it must be paranthesized
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