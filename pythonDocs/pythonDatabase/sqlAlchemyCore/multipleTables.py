from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

# Connection engine
engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/threedb', echo=True)

# Metadata object
metadata = MetaData()

# Define students table
students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(25)),
    Column('lastname', String(25)),
)

# Define addresses table
addresses = Table(
    'addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('student_id', Integer, ForeignKey('students.id'))
)

# Create tables in the database
metadata.create_all(engine)

# Define data to be inserted into students table
student_data = [
    {"name": "brian", "lastname": "mbugua"},
    {"name": "kimani", "lastname": "edgar"},
    {"name": "john", "lastname": "kinyanjui"}
]

# Insert data into students table
insert_into_students = students.insert().values(student_data)

# Create a connection and execute the insert statement for students table
with engine.begin() as connection:
    connection.execute(insert_into_students)

# Define data to be inserted into addresses table
address_data = [
    {"student_id": 1},
    {"student_id": 2},
    {"student_id": 3}
]

# Insert data into addresses table
insert_into_addresses = addresses.insert().values(address_data)

# Create a connection and execute the insert statement for addresses table
with engine.begin() as connection:
    connection.execute(insert_into_addresses)
