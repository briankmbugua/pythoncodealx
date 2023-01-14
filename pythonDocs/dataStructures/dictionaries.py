#!/bin/python3.9
"""Dictionaries are another built in data type in python unlike sequences which are indexed
by range of numbers dictionaries are indexed by keys, which can be any immutable type 
Strings and numbers can always be keys,Tuples can be used as keys if they contain only strings
 numbers or tuples, if a tuple contains any mutable object either directly or indirectly it 
 cannot be used as a key.It is best to think of dictionaries as key value pairs with the 
 requirment that keys are unique (within one dictionary)"""
 #operations on a dictionary
 #storing a value with some key and extracting the value given the key
 #it is also possible to delete a key:value pair with del, if you store with a key that arleady
 #exists the old value associated with that key is forgotten
 #it is an error to extract a value using non-existent key
 #Performing list(d) on a dictionary returns a list of all keys used in the dictionary in 
 #insertion order(if you want it sorted use sorted(d) instead)
 #to check whether a single key is the dictionary use the in keyword


tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
print(tel)
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)

#the dict() constructor builds dictionaries directly from sequences of key-value pairs
print(dict([('name', 'brian'),('age',26)]))

"""in addition, dict comprehensions can be used to create dictionaries from arbitrary key and
value expressions"""
print({x: x**2 for x in (2,4,6)})
#when the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments
print(dict(name="kim", guido=4127, age=900))