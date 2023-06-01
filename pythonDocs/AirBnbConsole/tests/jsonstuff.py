#!/usr/bin/python3

# json.dump()
"""
The json.dump() function is part of the python 'json' module and is used to serializee Python objects into a JSON formatted string and write to a file
"""
# SYNTAX
"""json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

obj - the python object to be serialized into JSON
fp - The file-like object(such as a file handle) where the JSON data will be written
"""

#XAMPLE USAGE
import json

data = {
    "name":"John",
    "age": 30,
    "city": "New York"
}

# Serialize the data and write it to a file
with open("data.json", "w") as file:
    json.dump(data, file)

# json.load
"""The json.load function is used to deserialize a JSON string or file-like object and convert it back into a Python object
"""

#SYNTAX
"""json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

fp - The file-like object such as a file handle containing the JSON data that needs to be deserialized
"""

# Rad the JSON data from a file and deserialize it
with open("data.json", "r") as file:
    data = json.load(file)

print(data)


