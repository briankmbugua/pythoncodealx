#!/bin/python3.9

#saving structured data with python
"""since read method only reads strings numbers have to be converted
to tring when writting them using a function like int() this processes is sloe
To save time python allows you to use JSON.The standard module called json can take python
hierachies and convert them to string represntations, this process is called serializing and
Reconstructing the data is called deserializing"""

import json
x = [1, 'simple', 'list']
#dumps() takes two arguments the data to be serialized and the file like object
#where the data will be written

print(json.dumps(x))

#another variant of dumps() dump() simply serializes the data into a text file
with open('data.json', 'w') as f:
    json.dump(x, f)

with open('data.json', 'r') as f:
    print(f.read())

#to decode the object again if f is a binary or a text file that has been opened for reading
with open('data.json', 'r') as d:
    x = json.load(d)
    print(x)

"""this simple serialization can handle lists and dictionaries, serialzing classes takes more
effort"""


