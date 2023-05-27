#!/usr/bin/python3
 
# The foundation for sql queries on the orm are Python objects that represent database concepts like tables, Columns.These objects are known collectively as database metadata.

# in sql the data holding structure which we query from is known as a table.In SQLAlchemy the database "table" is ultimately represented by a Python object similarly named Table.

from engine import engine
from sqlalchemy import MetaData
metadata_obj = MetaData()

# Once we have a MetaData object, we can declare some table objects

from sqlalchemy import Table, Column, Integer, String
user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key = True ),
    Column("name", String(30)),
    Column("fullname", String(30)),
)

#   When do i make MetaData object in my program?
# Having a single MetaData object for an entire application is the most common case, represented as a module-level variable in a single place in an application often in a 'models' or 'dbschema' type of package

# compents of a table
# Table - represents a database table and assings itself to a MetaData collection.
# Column - represents a column in a database table, and assings itself to a Table object.The column usually includes a string and a type object.The collection of Column objects in terms of the parent Table are typically accessed via an associative array located at Table.c:
print(user_table.c.name)
print(user_table.c.keys())

# Interger, String - these classes represent SQL datatypes and can be passed to a Column with or without necessarily being instantiatd.

# Declaring Simple Constrainsts
# The primary key itself is normally declared implicitly and is represented by the PrimaryKeyConstraint construct, which we can see on the Table.primary_key attribute on the Table object.
print(user_table.primary_key)
# The constraint that is most typically declared explicitly is the ForeignKeyConstraint object that corresponds to a database foreign key constraint.Below we declare a second table address that wil have a foreign key constraint referring to the user table.

from sqlalchemy import ForeignKey
address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable = False),
    Column("email_address", String(50), nullable=False),
)

# TIP 
# When using the Foreignkey object within a column defination, we can omit the datatype for that Column;it is automatically inferred from the related column, in the above example the Integer datatype of the user_account.id column.

# Emitting DDL to the Database
# We have an object structure that represents two database tables in a databse, starting at the root MetaData object.The into two Table objects, each of which hold onto a collection of Column and Constraint objects.Now we can emit CREATE TABLE statements.All the tools needed to do this are by invoking the Metadata.create_all() method on our MetaData, sending it to the engine that refers to the target database

metadata_obj.create_all(engine)


