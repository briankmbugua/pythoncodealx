# sqlAlchemy tutorial
## connection to the database(MySQL)
first import create_engine from sqlachemy
```python
from sqlalchemy import create_engine
# create engine
engine = create_engine('mysql+pymysql://<username>:<password>@<host>/<database_name>')
```
## example of a connection string
<span style ='color:yellow'>mysql+pymysql://root:password@127.0.0.1:3306/mydatabase</span>

# connection string
 - mysql+pymysql - specifies the MySQL dialect and the MySQL connector library to use in this case pymysql
- root - the username to use to connect to the MySQL server
- password - the password to use to connect to the MySQL server
- 127.0.0.1 - the ip address of the MySQL server in this case it is local
- 3306 - the port number on which the MySQL server is listening for connections the default port is 3306
- mydatabase - the name of the database to connect to.

# schema
A database schema is a blueprint of a database that defines the structure, organization, and relationships of the data.It is a logical representation of the database, not its pysical implementation.

# check version
```python
import sqlalchemy
print(sqlalchemy.__version__)
```

# SQLAlchemy Core - Expression Language
SQLAlchemy core includes
- SQL rendering engine
- DBAPI intergration
- transaction intergration
- schema description services

# Engine
Engine class connects a pool and Dialect togethor to provide a source of database connectivity and behaviour.An object of Engine class is instantiated using the create_engine() function.
## The most basic parameters of the create_engine() function are
- url: The URL of the database
- echo: A boolean value that specifies whether to echo SQL statements to the console
- echo_pool - A boolean value that specifies whether to echo SQL statements to the console when using a connection pool.
- echo_errors - a boolean value that specifies whether to echo errors to the console
- echo_warnings - a boolean value that specifies whether to echo warnings to the console
- pool_size - The size of the connection pool
- max_overflow - The maximum number of connections that can be created outside of the connection pool
```python
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://<username>:<password>@<host>/<dbname>")
# General sysntax
dialect+driver://<username>:<password>@<host>/<dbname>
```
The create_engine() function returns an Engine object.Some important methods of the Engine class are - 
- connect() - most important method. It returns a connection object that can be used to connect to the database.The connection object has methods that can be used to execute SQL statements, retrieve results and close the connection
- execute() - used to execute SQL statement.It takes a SQL statement as its first argument and a dictionary of parameters as its second argument.It retuens a ResultProxy object that can be used to retrieve the results of the statement.
- begin() - starts a transaction.A transaction is a unit of work that can be commited or rolled back.The begin method returns a Transaction object that can be used to commit or roll back the transaction
- commit() - commits a transaction.It commits the changes that have been made to the database since the transaction was started.
- rollback() - rolls back a transaction.It rolls back the changes that have been made to the database since the transaction was started.
- disspose() - closes the engine and releases any resources that it is using.This should be called when the engine is no longer needed.
- table_names() - Returns a list of all table names available in the database
- driver() - Driver name of the Dialect in use by the Engine

# SQLAlchemy Core - Creating Table
## Column object
SQLAlchemy Column object represents a column in a database table which is in turn represented by a Tableobject.
## Metadata
Is a container that holds a collection of 'Table' objects and their associated schema constructs.It's like a "bucket" that you can use to group related tables and their metadata togethor.
The MetaData object has an optional binding to an Engine pr a database connection this allows you to associate the Metadata object with a specific database so that you can easily create, modify and query tables using the Table objects in the Metadata

```python
from sqlalchemy import Metadata
meta = MetaData()
```
SQLAlchemy matches python data to the best possible generic column data types defined in it.
## Some generic data types
- BigInteger
- Boolean
- Date
- DateTime
- Float
- Integer
- Numeric
- SmallInteger
- String
- Text
- Time

## Example to create a students table in college database

```python
#importing everything required
from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
#creating a database engine or connection
engine = create_engine('mysql+pymsql://root:passowrd@127.0.0.1:3306/dbname')
#creating the metadata object from the MetaData() constructor
metadata = MetaData()
#creating the students table
students = Table(
    'students', metadata,#associating the table with the metadata object by passing it as an argument to the Table() constructor
    Column(id', Interger, primary_key = True), # creating the columns
    Column('name', String),
    Column('lastname', String)
)

metadata.create_all(engine)
```

## create_all()
When you define a Table object you're simply describing the structure of the table in your code.The Table object does't actually exist in the database untill you use the create_all() function to create it.
When create_all() is called it checks the metadata for any tables that haven't been created yet in the database and generates the sql code necessary to create those tables.It then executes the SQL code using the Engine object.Once all the tables have been created the metadata object is updated with information about those tables such as the primary key and the foreighn key contraints

