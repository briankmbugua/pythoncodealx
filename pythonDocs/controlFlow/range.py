#!/bin/python3
"""
if you need to iterate over a sequence of numbers, the built in range() function
comes in handy.
it generates arithmetic progressions
"""
for i in range(10):
    print(i)

"""
the given end point is never part of the generated sequence
it is possible to let range start at another number, or to specify the a different
increment(even negative, sometimes this is called the 'step')
"""
print(list(range(5, 10)))
print(list(range(0, 10, 2))) #zero is where to start from up to 10 not included and 2 is the step
                             #0,2,4,6,8
print(list(range(-10,-100, -30)))

"""
To iterate over the indices of a sequence, you can combine range() and len()
as follows
"""
a = ['mary','had','a','little','lamb']
for i in range(len(a)):
    print(i, a[i])
"""
a strange thing happens if you just print a range
"""

print(range(10))