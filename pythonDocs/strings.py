#!/bin/python3.9
"""
string literals can span multiple lines
"""
print("""\
    Usage:thingy[options]
    -h                        Display this message
    -H hostname               Hostname to connect to
""")
""""
strings can be indexed with the first character having index 0 indices may also be negative numbers
to start counting from the left
"""
word = "python"
print(word[0])
print(word[-2])

"""
slicing is also supported, slicing allows you to obtain a substring
"""
print(word[0:2]) #characters from position 0(included) to 2(exculed)
#note how the start is always included, and the ens=d always excluded
#this make sure that s[:i] + s[i:] is always equal to s
print(word[:2]+word[2:])
word[4:42] #'on'
word[42:]#'' out of range slice indexs are handled gracefully

#pyhton strings cannot be changed they are immutable
#word[0] = 'j'
#built in len() function returns the length of a string
print(len(word))