# Declare Mapping
First create_engine() function is called to establish a connection to the database
The engine establishes a real DBAPI connection to the database when a method like Engine.eecute() or Engine.connect() is called.
In case of ORM, the configuration process starts by describing the database tables and then by defining classes which will be mapped to those tables.
In SQLAlchemy these two tasks are perfomed togethor.This is done by using Declarative system; The classes created include directives to describe the actual database table they are mapped to.
A base class stores a catalog of classes and mapped tables in the Declarative system.This is called as the declarative base class.There will be usually one instance of this base in a commonly imported module.The declarative_base() function is used to create base class.This function is defined in sqlalchemy.ext.declarative module.

```python
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
```
once the base class is declared, any number of mapped classes can be defined in terms of it.

## defining a customers class, it contains the table to be mapped to and names and datatypes of columns in it.
```python
class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    address = Column(String)
    email = Column(String)
```

A class in Declarative must have a __tablename__ attribute, and at least one Column which is part of a primary key.
The information about class in Declarative system, is called as table metadata.
This MetaData object contains information about the database schema, including the tables, their columns, relationships, and constraints.
The MetaData object is accesible through the .metadata atrribute of the declarative base class('Base.metadata).It serves as a central repository for storing and managing the metadata information of the database schema.
The create_all() method of the 'MetaData' object is used to create the tables in the database based on the defined schema.
When you invoke Base.metadata.create_all(engine) you are instructing SQLAlchemy to create all the tables that have not been created yet in the connected database

```python
Base.metadata.create_all(engine)
```

# Creating Session
In order to interact with the database, we need to acces it's handle. A session object is the handle to the database.Session class is defined using sessionmaker() - a configurable session factory method which is bound to the engine object created earlier.

```python
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
```
The session object is then set up using it's default constructor as follows - 
```python
session = Session()
```
## frequently required methods of session class
- begin() - begins a transaction on this session
- add() - places an object in the session, its state is persisted on the database on the next flush operation.
- add_all() - adds a collection of objects to the session
- commit() - flushes all items and any transactions in progress
- delete() - marks a transaction as deleted
- execute() - executes a SQL expression
- expire() - marks an attribute of an instance as out of date
- flush() - flashes all object changes to the database
- invalidate() - closes connection using connection invalidation
- rollback() - rolls back the current transaction in progress
- close() - closes current session by clearing all items and ending any transaction in progress
- query() - it allows you to construct and execute queries against the database
 fetching the desired data.

 ## adding objects to the table
 