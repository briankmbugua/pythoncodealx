#!/usr/bin/python3.9
#NB
"""
When using regular expressions in python, it's recommended to use raw string notation(prefix the string with 'r') to avoid conflicts between the backslash character in the regular expression and in python string litrals,
Raw strings treat backslashes as literal characters, making it easier to write regular expressions
"""
#LIST OF METACHARACTERS
#  . ^ $ * + {} [] \ | ()
#1. Regularexpressions are used to match patterns in a string
#2. Most characters match themselves in regualar expressions, but there are special characters that have different meanings
#3. [ and ] are used to specify a character class, which is a set of characters to match
#4. The caret(^) inside a character class complements the set
#5. The backslash / is an important metcharacter that can be used to escape other metacharacters or signal special sequences
#6. Some special sequences are: \d, \D, \s, \S, \w, \W
#7.These sequences can be included inside a character class
#8. The metacharacter . matches any character except a newline, with the option to match even newlines (re.DOTALL)

#reapeating things
#THE '*' Metacharacter
# the '*' character in python regular expressions is a special character that matches zero or more occurences of the preceding character or group, it can be used to match preceding  characters in strings
#example in the pattern 'ca*t' here you want to match 'a' zero or more times 'ct'(0 'a' characters), cat(1 'a'), 'caaat' (3, 'a')


#THE '+' Metacharacter
# The '+' symbol means to match one or more occurences of the preceding character or group, in the pattern  ca+t will match 'cat'(1 'a'), 'caat'(3 'a' s) but won't match 'ct' since there is not a single a

#THE ? character
# The '?' means to match either once or zero times, it's making something as being optional
#example--- home-?brew this matches either homebrew or home-brew

#{m,n} quantifier, where m and n are decimal intergers, this quantifier means that there must be atleast m repetitions and at most n, For example a/{1,3}b will match 'a/b', 'a//b', and 'a///b', it won't match 'ab' which has no slashes or 'a////b' which has four
#You can omit m or n, a resonable value is assumed for the missing value, omitting m is interpreted as a lower limit of 0, while omitting n results in an upper bound of infinity
#{0,} is the same as *, since it means zero to infinity, {1,} is equivalent to +, since it means atleast once to infinity, and {0,1} is the same as ? since it means match zero or 1

#USING REGUALR EXPRESSIONS
#The re modules provides an interface to the regular expressions engine, allowing for compilation of REs into objects and then perform matches with them

#Compling Regular Expressions
#REs are compiled into pattern objects, which have methods for various ops such as searching for pattern matches or perfoming string substitutions

import re #interface for regex engine

p = re.compile('ab*', re.IGNORECASE) #re.compile() accepts optional args
print(p)

#RE is passed to re.compile() as a string, this brings the Backslash Plague

#Backslash Plague
