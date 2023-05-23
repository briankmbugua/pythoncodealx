#!/usr/bin/python3
from sqlalchemy import create_engine;
#create engine
engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/record_company');

#create connection
conn = engine.connect()

# check if connection is succesful
if conn:
    print('Database connected succesfully')
else:
    print('Connection failed');

#close connection
conn.close();