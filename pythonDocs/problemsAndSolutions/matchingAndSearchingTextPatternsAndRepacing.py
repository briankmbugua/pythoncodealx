#!/usr/bin/python3
#PROBLEM
"""You want to match or search text for a specific pattern"""
#SOLUTION
"""If the text you are matching is a simple literal, you can often just use the basic string methods such str.find(), str.endswith(), str.startswith() or similar"""

#EXCAT MATCH
text = "yeah, but no, but yeah, but no, but yeah"
print(text == 'yeah')

#SEARCH FOR THE LOCATION OF THE FIRST OCCURENCE
print(text.find('no'))

# for more complicated matching use regular expressions
#SEARCHING AND REPLACING TEXT
#PROBLEM
"""you want to search and replace a text pattern in a string"""
#for simple litral patterns use str.replace() method

print(text.replace('yeah', 'yep'))

#for more complicated patterns use the sub() function/method in the re module.

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))#the first argument to sub() is the pattern to match and the second argument is the replacement pattern.There isn't much more to regular expression search and replace than the sub() method shown.The trickiest part is specifying regular expression pattern.
