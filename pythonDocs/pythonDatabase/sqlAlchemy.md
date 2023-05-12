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