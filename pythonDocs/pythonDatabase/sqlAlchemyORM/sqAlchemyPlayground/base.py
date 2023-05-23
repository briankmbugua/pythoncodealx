from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
#create engine
engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/dbthree', echo=True)
#base class
Base = declarative_base()

#creating customers table
class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True) # autoincrement=True is the dafault behaviour for primary key columns in SQLAlchemy.However explicitly setting it can make your intentions clearer and ensures consistent behaviour across different database backends

    name = Column(String(25))
    address = Column(String(25))
    email = Column(String(25))

Base.metadata.create_all(engine)

"""
When executed, Python console will echo the following SQL expression being executed
CREATE TABLE customers (
    id INTERGER NOT NULL,
    name VARCHAR,
    address VARCHAR,
    email VARCHAR,
    PRIMARY KEY (id)
)
"""