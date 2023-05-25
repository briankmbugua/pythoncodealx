#!/usr/bin/python3
from engine import engine
from sqlalchemy import text
# We can declare our connect block to be a tranasaction block upfront.
# For this mode of operation we use the Egine.begin() method.This method will both manage the scope of the Connection and also enclose everything inside a transaction with commit at the end assuming a successful block, or ROLLBACK in case of exception raise.

# "begin once"
with engine.begin() as conn:
    conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),[{"x":6, "y":8}, {"x": 9, "y": 10}],)

