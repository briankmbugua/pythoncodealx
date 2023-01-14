#!/bin/python3.9
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.index('banana', 4))  # Find next banana starting at position 4
print(fruits.index('banana'))
print(fruits.count('tangerine'))
print(fruits.count('apple'))
print(fruits)
print("AFTER REVERSING")
print(fruits.reverse())
print(fruits)
fruits.append('grape')
print(fruits)
print("AFTER SORTING")
fruits.sort()
print(fruits)
print("AFTER POP")
fruits.pop()
print(fruits)

"""you may have noticed that methods like insert,remove or sort that only modify the
list have no return value printed - they return default None.This is a desing principal
for all mutable data structures in python"""

#USING LISTS AS STACKS
"""the list methods make it very easy to use a list as a stack, where the last element
added is the first element retrieved("last-in, first-out") lists are not efficient for this purpose
While appends and pops from the end of the list are fast, doing inserts or pops from the beggining
of a list slow To implement stack use collecions.deque which was desinged to have fast appends and
pops from both ends"""
from collections import deque

queue = deque(['ERIC','JOHN','MICHAEL'])
queue.append('TERRY') #TERRY  arrives
queue.append("graham") #graham arrives
print(queue.popleft()) #the first to arrive now leaves
print(queue.popleft()) #the second to arrive now leaves
print(queue) #remaining queue in order of arrival

#list comprehession
"""list comprehesions provide a concise way to create lists."""
#e.g create a list of squares
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

"""the above creates or overwrites a variable named x that still exists after the loop completes
we can calculate the list of squares without any side effect using"""
squares = list(map(lambda x: x**2, range(10)))#map is an inbuilt function that applies a given function
#to each member of an iterable(list,tuple,set,etc) and returns an iterator
#list is a constructor for list data structure
print(squares)
"or equivalently"
squares = [x**2 for x in range(10)]
print(squares)
