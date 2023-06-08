#!/usr/bin/python3
#PROBLEM
"""YOU NEED TO SPLIT S STRING INTO FIELDS, BUT THE DELIMITERS AND SPACING AROUND THEM AREN'T CONSISTENT THROUGHT THE STRING"""
#SOLUTION
"""THE split() method of string objects is really meant for very simple cases and does not allow for multiple delimeters or account for possible whitespace around the delimeters in this case you need a bit more flexibility, use the re.split() method"""

line = 'asdf fjdk; afed, fjek, asdf,      foo'

import re

fields = re.split(r'[;,\s]\s*', line)

print(fields)

#DISCUSSION
"""The re.split() function is useful coz you can specify multiple patterns for the separator.Above the separator is either a comma(,),semicolon(;), or whitespace followed by any amount of extra white space"""

fields = re.split(r'(;|,|\s)\s*', line)

print(fields)

"""Getting the split characters is useful in certain contexts"""

values = fields[::2]
delimeters = fields[1::2] + ['']
print(f"VALUES {values}")
print(f"DELIMETERS {delimeters}")

# REFORM THE LINE USING THE SAME DELIMETERS
reformedString = ''.join(v+d for v, d in zip(values, delimeters))

print(reformedString)

"""If you don't want the separator characters in the result but still need to use parentheses to group parts of the regular expression pattern, make sure you use a noncapture group specified as (?:....)"""

fields = re.split(r'(?:,|;|\s)\s*', line)

print(fields)


