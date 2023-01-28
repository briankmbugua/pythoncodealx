#!/bin/python3.9
"""python also includes a data type for sets.A set is an unordered collection with no duplicate
elements.Basic uses include membership testing and eliminating duplicate entries Set objects
also support mathematical operations like union, difference, and symmetric difference
Curly braces or the set() function can be used to create sets.NB to create an empty set
you have to use set() not {} the latter creates an empty dictionary"""

#brief demonstration
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) #duplicate elements have been removed
print('orange' in basket)
print('mandizi' in basket) #fast membership testing
#Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)#unique letters in a
print(a-b) #letters in a but not in b
print(a | b) #letters in a or b or both
print(a & b)#letters in both a and b
print(a ^ b) #letters in a or b not both

"Similarly to list comprehensions, set comprehensions are also supported"
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
print(a)
