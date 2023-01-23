#!/bin/python3.9

"""some objects defined standard clean-up actions to be undertaken when an object is no longer
needed, regardless of whether or not the operation using the object succeeded or failed"""
#example

for line in open('myfile.txt'):
    print(line, end=' ')

"""this leaves the file open for a long time,use 'with' statement it allows objects
like files to be used in a way that ensures they are always cleaned up"""

with open('myfile.txt') as f:
    for line in f:
        print(line, end='')
#After the statement is executed, the file f is always closed
#objects which require predifined clean up actions will indicate that in their docs
