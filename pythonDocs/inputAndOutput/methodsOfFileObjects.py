#!/bin/python3.9

f = open('workfile.txt','r',encoding='utf-8')

#f.read(size) which reads some quantity of data and returns it as a string(in text mode)
#or bytes object (in binary mode) size is an optional numeric argument
#print(f.read(10))
#print('f')
#print(f.read())#reads the entire file and puts the file pointer at the end therefore
#any attempts to use readline() will return an empty string since the pointer is already at
#the end and there is no more file to read

#f.readline() reads a single line from the file:a newline character is left at the end of the
#line and is only ommited on the last line if the doesn't end in a newline
print('READ LINE')
print(f.readline())#will return an empty string since f.read() has already been used above it
                   #comment any f.read() above this to see the output of f.readline()
                   #if you want to use f.read() and f.readline() in the same file use f.seek()
                   #which takes an interger argument that represents the position in the file 
                   #to move the pointer to

print(f.readline()) #will output the second line
print(f.readline()) #will output an empty string since there is no third line





s = open('read.txt','r',encoding='utf-8')
#you can loop over the file object this memory efficient,fast and leads to simple code
for line in s:
    print(line)

#if you want to read all the lines of a file use list(f) or f.readlines
print(list(s)) #['first line\n', 'second line'] to see this comment for line in s
print(s.readlines())
f.close()

