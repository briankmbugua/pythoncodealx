#!/usr/bin/python3
from model_state import Base
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
        engine = create_engine('mysql+pymysql://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True, echo=True)
        Base.metadata.create_all(engine)

"""
EXPLANATION FOR THE ABOVE CODE
We import base from model_state which has the Base class and table defination
We also import create_engine, it is used to create an engine object that represents the interface to a particular database.It takes the database URL as an argument and returns an Engine class
## SYNTAX
create_engine(url, **kwargs)
url - The url argument is a string that specifies the connection details for the database.It typically follows a specific format known as a database URL.The format depends on the database you are connecting to.
**kwargs - The **kwargs allows you to provide keyword arguments to configure the behaviour of the engine.commonly used keyword arguments include
- echo -- When set to true it enables verbose output of SQL statements and database instructions.This can be helpful for debugging purposes.
- pool_size -- Specifies the size of the connection pool.The connection pool allows reusing connections to improve performance
- max_overflow -- Specifies the number of connections that can be created beyond the pool_size limit.This can be useful in handling sudden spikes in connection requests
- pool_pre_ping -- When set to true it enables a mechanism to the check the connection health before using it.This can help detect and recover from database connection issues.
"""
