#!/usr/bin/python3.9
#continued from doctest_unpredictable.py
#There are cases where the unpredictable value cannot be ignored
#when dealing with data types whose string representations are inconsistent, e.g the string form of a dictionary may change based on the order the keys are added

keys = ['a', 'aa', 'aaa']
print('dict', {k: len(k) for k in keys})
print('set :', set(keys))
