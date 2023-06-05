#!/usr/bin/python3
#DEFINATION AND USAGE
"""The replace() methods replaces a specified pharase with another specified phrase, All occurences of a specified pharase will be replaced, if nothing else is specified"""
#SYNTAX
"""string.replace(oldvalue, newvalue, count)
oldvalue  - Required. The string to search for
newvalue - Required. The string to replace the old value
count - Optional, a number specifying how many occurences of the old value you want to replace.Default is all occurences"""
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

# Replace all the occurences of the word one
x = txt.replace("one", "three")
print(x)
