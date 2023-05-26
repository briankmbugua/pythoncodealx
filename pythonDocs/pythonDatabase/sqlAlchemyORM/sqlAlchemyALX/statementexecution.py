#!/usr/bin/python3
#in statement execution we make use of a method called Connection.execute(), in conjuction with an object called text(), and returning an object called Result.

# Fetching Rows
from engine import engine
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x} y: {row.y}")

# The "SELECT" string we executed selected all rows from our table.The object returned is called Result and represents an iterable object or result rows.
# Result has a lot of methods for fetching and transforming rows, such as Result.all() method illustrated previously, which returns a list of all Row objects.It also implements the python iterator interface so that we can iterate over the collection of Row objects directly.

# The Row objects themselves are intended to act like Pyhon named tuples.

# Tuple Assingment
with engine.connect() as connection:
    result = connection.execute(text("select x, y from some_table"))
    for x, y in result:
        print(x)
        print(y)

# Interger index - Tuples are Python sequences, so regular interger access is available too

with engine.connect() as connection:
    result = connection.execute(text("select x, y from some_table"))
    for row in result:
        x = row[0]
        print("X:",x)



