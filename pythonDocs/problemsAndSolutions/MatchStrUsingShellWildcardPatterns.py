#!/usr/bin/python3
"""Problem you want to match text using the same wildcard patterns as are commonly used when working in Unix shells (e.g, *.py, Dat[0-9]*.csv, etc)"""

#SOLUTION
"""The fnmatch module provides two functions--fnmatch() and fnmatchcase() that can be used to perfom such matching."""

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv','Dat[0-9]*'))


names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']

print([name for name in names if fnmatch(name, 'Dat*.csv')])

#USE fnmatchcase where there is case sensitivity

print(fnmatch('foo.txt', '*.TXT')) # on linux this will be false on windows it will be true in this case use fnmatchcase()
print(fnmatchcase('foo.txt', '*.TXT'))


"""An often overlooked feature of these functions is their potential use with data processing of nonfilenames strings.E.G a list of street addresses like this"""

addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]

"""You could write list comprehensions like this"""

print([addr for addr in addresses if fnmatchcase(addr, '* ST')])

print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

#DISCUSSION
"""The matching perfomed by fnmatch sits somewhere between the functionality of simple string methods and the full power of regular expressions"""
