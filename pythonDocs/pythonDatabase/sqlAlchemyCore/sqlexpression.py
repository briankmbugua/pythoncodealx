from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


#create an engine and connect to the database

engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/twodb', echo=True)


#create a MetaData object

metadata = MetaData()

# define a table called students

students = Table('students', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String(25)),
                 Column('lastname', String(25)),
                 )

#create the tables in the database

metadata.create_all(engine)

# create an insert object for the "students" table

insertStatement = students.insert().values(id=1,name="brian",lastname="mbugua")

#print the generated SQL statement
print(str(insertStatement))

# Acces the parameter values in the compiled statement, params is dictionary

params = insertStatement.compile().params

print(params)

with engine.begin() as conn:
    conn.execute(insertStatement)

# results
# connection = engine.connect()
# result = connection.execute(insertStatement)

# print(result)

