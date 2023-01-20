#!/bin/python3.9

#Reading and Writting Files

"""open() returns a file object, and is most commonly used with two positional arguments and 
one keyword argument  open(filename, mode, encoding=None)"""

f = open('workfile.txt', 'r', encoding='utf-8')
print(f.read())
print(f.closed)
f.close()#you must manually free any resources used to read the file if you are not using with
print(f.closed)
"""The first argument is a string containing the filename, the second is a string describing 
the way the file will be used
'r'--- read file, 'w'--- writting only and any existing file with the same name will be erased
'a'--- opend the file for appending any data written to the file is automatically added at the 
end, 'r+'--- opens the file for both reading and writting, 'rb+' --- means open for write and
reading in binary, the '+' makes it write and reading the mode argument is optional and
when ommitted 'r' is will be assumed
UTF-8 is the modern de-facto standard
Appending a 'b' to the mode opens the file in binary mode, in binary mode the data is read and
written as bytes objects, you cannot specify encoding when opening in binary mode
It is good practice to use the with keyword when dealing with the file objects.The advantage
is that the file is properly closed after its suite finishes, even if an exeption is raised at
some point it is better than using try-finally blocks"""

with open('workfile.txt', encoding='utf-8') as f:
    read_data = f.read()
    print(read_data)

print(f.closed) #output is True
"""if you are not using the with keyword, then you should call f.close() to close the file and
immediately free up any system resources used by it
After a file object is closed with either by a with statement or by calling f.close(), attempts
to use the file object will automatically fail"""

#METHODS OF FILE OBJECTS

