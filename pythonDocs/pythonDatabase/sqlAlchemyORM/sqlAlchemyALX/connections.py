#!/usr/bin/python3
#The engine interactive endpoinsts the Connection and Result, Additionaly there is ORM's facade for these objects, known as Session
# Getting a Connection
# The Engine object's main purpose is to provide a connection to the database called a Connection
# The Connection object is used for all interactions with the database when working with the Core directly
# It is important to limit the scope of the Connection object to a specific context since the Connection represents an open resource against the database.

from sqlalchemy import create_engine
from sqlalchemy import text
from engine import engine
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
