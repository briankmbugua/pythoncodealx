#!/usr/bin/python3
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/sqlAlchemydb')

metadata = MetaData()

users = Table('users', metadata, 
              Column('id', Integer, primary_key=True),
              Column('name', String(50)),
              Column('age', Integer),
              Column('email', String(50)))

metadata.create_all(engine)

# with engine.connect() as conn:
#     conn.execute(users.insert().values(name='Alice', age=25, email='alice@mail.com'))
#     conn.execute(users.insert().values(name='Bob', age=30, email='bob@mail.com'))

from sqlalchemy import select

with engine.connect() as conn:
    result = conn.execute(select(users))
    for row in result:
        print(row)



