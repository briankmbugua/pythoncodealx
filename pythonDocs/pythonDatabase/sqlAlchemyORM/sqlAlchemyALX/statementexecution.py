#!/usr/bin/python3
#in statement execution we make use of a method called Connection.execute(), in conjuction with an object called text(), and returning an object called Result.

# Fetching Rows
from engine import engine
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x} y: {row.y}")
