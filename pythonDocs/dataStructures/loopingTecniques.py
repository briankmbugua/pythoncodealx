#!/bin/python3.9


#looping techniques
"""when looping through dictionaries, the key and the corresponding value can be retrieved
at the same time usig items() method"""

knights = {'gallahad':'the pure','robin':'the brave'}
for k, v in knights.items():
    print(k, v)

"""when looping through a sequence you can retrieve the index and item using the 
enumerate() function
"""

for i, v in enumerate(['tic','tac','toe']):
    print(i, v)

"""to loop over two entries at the same time, the entries can be paired using
the zip() function"""

questions = ['name','quest','favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q,a))

"""to loop over a sequence in reverse, first specify the sequence in foward direction and then
call the reversed() function"""

for i in reversed(range(1, 10, 2)):
    print(i)

"""to loop over a sequence in sorted order use the sorted() function which returns a new sorted list
while leaving the source unaltered"""

basket = ['apple','orange','apple','pear','orange','banana']
for i in sorted(basket):
    print(i)

"""Using set() on a sequence eliminates duplicate elements.The use of sorted() in combination
with set() over a sequence is an idiomatic way to loop over unique elements of the sequence
in sorted order"""

for f in sorted(set(basket)):
    print(f)

"""it is sometimes tempting to change a list while you are looping over it, however it is often
simpler and safer to create a new list instead"""

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

#MORE ON CONDITIONS
"""the conditions used in while and if statements can contain any operators, not just
comparisons you can also use any other operators functions or callable in these conditions
as long as they evaluate to a boolean valur(True of False)"""
#in an if statement, you can use mathematical operators to check if a number is odd or even:
x = 5
if x % 2 == 1:
    print("x is odd")
else:
    print("x is even")

#In a while statement, you can use logical operators to check multiple conditions:
x = 0
while x < 5 and x % 2 == 0:
    print(x)
    x += 1

"""The comparison operators in and not in are membership test that determine whether a value
in or not in a container, is and is not compare whether two objects are really the same object"""
#you can use an 'in' operator to check if an element is in a list:
numbers = [1,2,3,4,5]
if 3 in numbers:
    print('3 is in the list')
else:
    print('3 is not in the list')

#the 'not in' operator can be used to check if an element is not in a container
if 6 not in numbers:
    print("6 is not in the list")
else:
    print('6 is in the list')

""" 'is' and 'is not' operators are used to compare whether two objects are the same in memory,
not just having the same value"""

x = [1,2,3]
y = [1,2,3]

z = x
print(x == y) #True they have the same value
print(x is y) #False they are not the same objects in memory
print(x is z) #z and x are the same object in memory

"""Copmarisons can be chained. a < b == c test whether a is less than b and moreover b equals c"""

a = 5
b = 10
c = 15

# Chained comparison using 'and' operator
if a < b and b == c:
    print("a is less than b and b is equal to c")
else:
    print("a is not less than b or b is not equal to c")

"""comparisons may be combined using the boolean operators 'and' and 'or' and the outcome of 
a comparison(or any other boolean expression) may be negeted using not.These have lower priorities
than comparison operators, between them not has the highest priority and or the lowest
so that "A and not B or C" IS EQUIVALENT TO " (A and (not B) or C) " """
#change the values in A,B,C and in the print to see the results
A = True
B = True
C = False
print(A and B or C)
print((A and (not B) or C))

#its possible to assing the result of a comparison operator or other Boolean expressions to 
#a variable

#change the values of the strings to see different outputs
string1, string2, string3 = '', '', 'mbugua'
no_null = string1 or string2 or string3
print(no_null)