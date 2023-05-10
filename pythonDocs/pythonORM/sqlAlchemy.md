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