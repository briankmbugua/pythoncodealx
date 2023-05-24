# The start of any SQLAlchemy application is an object called the Engine.
# The Engine serves as a source of connections to a specific database.
# It acts as both a factory and a connection pool for these database connections.
# The Engine is usually a global object created once for a specific database server.
# It is configured using a URL string that describes the connection details to the database host or backend.

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:password@localhost:3306/onedb',pool_pre_ping=True,echo=True)
# Kind of database that we are communicating with in this case it is mysql
# What DBAPI are we using,This is a third party driver that SQLAlchemy uses to interact with a particular database.If omitted, SQLAlchemy will use a default DBAPI for the particular database in this case we are using pymysql
# How do we locate the database, in this case our URL ://root:password@localhost:3306/dbone

# Lazy Connecting
# The engine when first returned by create_engine(), has not actually tried to connect to the database yet, that happens only the first time it is asked to perform a task against the database.This is a software desing pattern know as lazy initialization
# create_engine.echo will instruct the Engine to log all the SQL it emits to a pyhton logger.
