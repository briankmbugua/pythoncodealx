from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

#create a conection engine
engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/threedb', echo=True)

#create a Metadata object and bind to the engine

metadata = MetaData()


#create a table and associate to the metadata object

users = Table('users', metadata,
              Column('id', Integer),
              Column('name', String(25)),
              )
# create all tables defined in the metadata

metadata.create_all(engine)


# Insert data into the "users" table

insertStatement = users.insert().values(id = 1, name = "brian")

# Execute the insert statement
with engine.begin() as conn:
    conn.execute(insertStatement)

