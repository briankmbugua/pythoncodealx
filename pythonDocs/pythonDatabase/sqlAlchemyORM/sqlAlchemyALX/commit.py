#!/usr/bin/python3
from engine import engine
from sqlalchemy import text
# DBAPI connection is not-autocommiting we will create a table and insert some data and the transaction is then commited using the Connection.commit() method, invoked inside the block where we acquired the Connection object.

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table(x int, y int)"))
    conn.execute(text("INSERT INTO some_table (x,y) VALUES(:x, :y)"),
                 [{"x":1, "y":1}, {"x":2, "y":4}],)
    conn.commit()

#Above, we emmited two SQL statements that are generally transactional a 'CREATE TABLE' statement and an 'INSERT' statement.As we want the work we've done to be commited within our block we invoke the Connection.commit() method which commits the transaction.After we call this method inside the block, we can continue to run more SQL statements and if we choose we may call Connection.commit() again for subsequent statements.SQLAlchemy refers to this style as commit as you go.