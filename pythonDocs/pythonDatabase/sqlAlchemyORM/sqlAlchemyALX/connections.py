#!/usr/bin/python3
#The engine interactive endpoinsts the Connection and Result, Additionaly there is ORM's facade for these objects, known as Session
# Getting a Connection
# The Engine object's main purpose is to provide a connection to the database called a Connection
# The Connection object is used for all interactions with the database when working with the Core directly
# It is important to limit the scope of the Connection object to a specific context since the Connection represents an open resource against the database.
from sqlalchemy import text
from engine import engine
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

#The context manager in this case with provided for a database connection and also framed the operation inside of a transaction. The default behaviour of the Python DBAPI includes that the transaction is always in progress When the scope of the connection is released, a ROLLBACK is emitted to end the transaction.The transaction is not commited automatically when we want to commit data we normally need to call Connection.commit()
#The result of our SELECT was also returned in an object called Result.It is best to ensure this object is consumed within the connect block and is not passed along outsode the scope of our connection.