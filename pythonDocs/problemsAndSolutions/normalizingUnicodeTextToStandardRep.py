#!/usr/bin/python3
# PROBLEM
"""you are working with Unicode strings, but need to make sure that all of the strings have the same underlying representation"""
# SOLUTION
"""In unicode certain characters can be represented by more than one valid sequence of code points.To illustrate consider"""
import unicodedata
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1)
print(s2)
print(
    f"The length of String1 is - {len(s1)} and the length of string2 is - {len(s2)}")
print(f"testing equality of s1 and s2 {s1 == s2}")
"""To have multiple representations is a problem for programs that compare strings.In order to fix this you should first normalize the text into a standard representation using the unicodedata module"""

t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1)
print(t2)
print(f"The length of  normalized String1 is - {len(t1)} and the length of normalized string2 is - {len(t2)}")
print(f"testing equality of  normalized s1 and s2 {t1 == t2}")
