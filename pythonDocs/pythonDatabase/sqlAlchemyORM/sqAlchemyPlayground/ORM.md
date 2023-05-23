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
 After declaring a mapping and creating sessions next you add objects to the table
 ```python
 c1 = Sales(name = "brian")
 session.add(c1)
 ```
 The transaction above is pending untill the same is flushed using commit() method.
  ```python
 c1 = Sales(name = "brian")
 session.add(c1)
 session.commit()
 ```
 When you call session.commit() SQLAlchemy initiates a flush operation.
 When you make changes to objects within a session, SQLAlchemy keeps track of these changes in memory.However the changes are not immediately written to the database. They are accumulated and held in the session's transactional context.
 During the flash SQLAlchemy generates the necessary SQL statements based on the tracked changes and sends them to the database for execution.All the CRUD operations. This ensures ACID
 ## ACID
 - Atomicity - Guarantess that a transaction is treated as a single indivisible unit of work.It means that either all changes made within one transaction are commited successfully, or none of them are commited at all.If any part of the transaction fails or encounters an error, the entire transaction is rolled back.
 - Consistency - Ensures that a transaction brings the database from one consistent to another consistent state.This guarantees that the integrity of the data is maintained throught the transaction.
 - Isolation - Ensures that concurrent transactions do not interfere with each other while accessing the or modifying the database.Each transaction is executed in isolation as if it were the only transadtion taking place.
- Durability - Guarantess that once a transaction is committed, its changes are permanently saved and will survive any subsequent failures.

# SQLAlchemy ORM - Using Query
All SELECT statements generated by SQLAchemy are constructed by Query object.
It provides a generative interface.

## QUERY OBJECTS
Query objects are initially generated using the query() method of the Session as follows-
```python
query = session.query(mapped class)
```
The following is also equivalent to the above given statement
```python
query = Query(mappedClass, session)
```
The query object has all() method which returns a result set in the form of list of objects.
```python
result = session.query(Customers).all()
```
The above statement is equal to the following SQL statement
```sql
SELECT * FROM Customers
```
The mappedClass parameter refers to the class that is mapped to a specific database table using SQLAlchemy ORM.It identifies the table you want to Query or perfom operations on when creating a Query object

## GENERATIVE INTERFACE
Each call to a method on the Query object returns a new Query object.This new Query object is a copy of the previous one, but with additional criterial and options associated with it.
In practical terms it means you can chaim multiple method calls on a Query object to progressively build up the desired Query.
## Example
```python
query = session.query(User).filter(User.age >= 18).order_by(User.name)
```
In the above example we start with a base Query object by calling session.query(User)
Then, we chain the filter() method to add a condition that filters users based on their age being grater than or equal to 18.Finally, we chain the 'order_by()' method to sort the results by the user's name.

## USEFUL QUERY METHODS
- add_columns - it adds one or more column expressions to the list of result columns to be returned
- add_entity() - it adds a mapped entity to the list of result columns to be returned.
- count() - returns a count of rows this Query would return
delete() - it perfoms a bulk delete query.Delete rows matched by this query from the database
- distinct() - it applies a DISTINCT cluase to the query and return the newly resulting Query
- filter() - applies the given filtering criterion to a copy of this query, using SQL expressions
- get() - returns an instance based on the given primary key indentifier providing direct access to the identity map of the owning session
- group_by() - returns one or more groups by criterion and apply generatively, returning the newly resulting query
- one() - It returns excatly one result of raise an exception
- order_by() - it applies one or more ORDERED BY criterion to the query and returns the newly resulting Query
- update() - performs a bulk update query and updates rows matched by this query in the database.
# CRUD
### create
use session.add() to add objects
session.commit() to persist changes to the database
### read
To retrieve data use session.query() with any filters, joins or sorting options
### update
You retrieve an existing object from the database using query or any other means
You the modify the attributes of the object with the desired values
Then use session.commit() to persist the changes in the database

```python
# update example
#Assuming 'session' is an instance of SQLAlchemy session and customers is a mapped class
#Retrieve the customer to update
customer = session.query(Customer).filter_by(id=1).first()
#update the customer's attributes
customer.name = "New Name"
customer.email = "newemail@example.com"
#commit changes to the database
session.commit()
```
### delete
First retrieve the object representing the record from the database using a query or any other means, Then call session.delete() passing in the object to mark it for deletion.
session.commit() will remove it from the databasa
```python
customer = session.query(Customer).filter_by(id=1).first()
# Delete the customer
session.delete(customer)
# Commit changes to the database
session.commit()
```

# SQLAlchemy ORM - Building relationships

