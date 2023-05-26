#!/usr/bin/python3
#The fundamental transaction/database interactive object when using the ORM is called the Session.
#The Session has a few different creational patterns, the most basic one that tracks exactly with how the Connection is used which is to construct it within a context manager.
from engine import engine
from sqlalchemy.orm import Session
from sqlalchemy import text

session = Session(bind = engine)

statement = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")


with session as session:
    result = session.execute(statement, {"y": 6})
    for row in result:
        print(f"x: {row.x} y {row.y}")


with session as session:
    result = session.execute(text("UPDATE some_table SET y=:y WHERE x=:x"),[{"x":9, "y":11}, {"x":13, "y": 15}],)
    session.commit()

#TIP
#The session doesen't actually hold onto the connection object after it ends the transaction.It gets a new connection from the engine the next time it needs to execute SQL against the database

