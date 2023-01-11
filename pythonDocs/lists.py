#!/bin/python3
"""
list can be written as a list of comma separated values between square
brackets [] list might contain different types, but usually the items 
all have the same type
"""

squares = [1,4,9,16,25]
print(squares)

#like strings (and all other built-in sequence types), lists can be indexed and sliced
#slicing returns a new string, all slice operations returns a new list containing the requested
#elements
print(squares[0])
print(squares[-1]) #returns the last item
#shallow copy
print(squares[:])
#lists also suppor operations like concatenation
print(squares + [100, 200])
#unlike strings which are immutable, list are a mutable type
cubes = [1,2,3]
cubes[0] = 30
print(cubes)
#you can also add new items at the end using the append method
cubes.append(2*7)
print(cubes)
#assingment to lists is also possible
letters = ['a','b','c','d']
print(letters)
letters[2:5] = ['A','B','C']
print(letters)
letters[2:5] = []
print(letters)
#clear the list by replacing all elements
letters[:] = []
print(letters)
#built in length also applies to lists
name = ['b','r']
print(len(name))

#it is also possible to nests lists
a = ['a','b','c','d']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0])
print(x[0][1])


#print()

"""
the print() function writes the value of the argument(s) it's given
the keyword end can be used to avoid newline after the output or end the
output with a different string
"""
z, c = 0, 1 #same as z = 0 and c = 1
print(z)
while z < 10:
    print(z, end = ',')
    z, c = c, z+c #same as z = c and c = z+c