#!/bin/python3.9

#f.write()
"""
f.write(string) writes the contents of a string to the file, returning the number of
characters written
"""
f = open('write.txt','w',encoding='utf-8')
print(f.write('This is a test\n')) #no of characters written

"""other types of objects need to be converted - either to a string(in text mode)
or bytes object(in binary mode) before writting them"""
value = ('the answer', 42)
s = str(value) #convert the tuple to a string
f.write(s)

"""
Appending a 'b' to the mode opens the file in binary mode, in binary mode the data is read and
written as bytes objects, you cannot specify encoding when opening in binary mode
"""
"""f.tell() returns an interger giving the file object's curren position
#in the file represented as number of bytes from the beginning of the
#file when in binary mode and an opaque number when in text mode"""

print(f.tell())


"""f.seek(offset, whence) used to change the file object's position, The position is 
calculated from adding offset to a reference point the reference point
is selected by the whence argument
A whence value of 0 measures from the beggining of a file
1 uses the current file position
2 uses the end of the file as the reference point, whence can be ommited and defaults to 0,"""

f = open('workfile2.txt', 'rb+') #open the file in binary for read and writting
print(f.write(b'0123456789abcdef'))#the b hear means this is a bytes literal, a sequence of bytes
                                   #represented as ASCII characters, the contents of the byte litral
                                   #will be written as they are in a file opened in binary mode
print(f.seek(5)) #go to the 6th byte of the file
print(f.read(1))
print(f.seek(-3, 2))#2 means the end thus (-3, 2) means go to the 3rd byte before the end
print(f.read(1))

"""
in text files those opened without a b only seeks relative to the beginning of the file
are allowed exception beong seeking to the very end of the file with seek(0, 2) and the only
valid offset values are those returned by f.tell() or zero
"""