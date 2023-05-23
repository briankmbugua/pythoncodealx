from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/dbthree', echo=True)
from sqlalchemy.orm import declarative_base

# base class which all tables will be based on
Base = declarative_base()
# customers table
class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)
# creating a handle to the database using sessionmaker
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

customer1 = Customers(name = "brian mbugua", address = "Boma road kiambu", email = "briankmbuguak@gmail.com")


session.add(customer1)

customers = [
    Customers(name = 'Komal Pande', address = 'Koti, Hyderabad', email = 'komal@gmail.com'),
    Customers(name = 'Susan muthoni', address = 'naivasha', email = 'susan@gmail.com'),
    Customers(name = 'Oscar njenga', address = 'kathpat', email = 'oscar@gmail.com')
    ]
session.add_all(customers)
session.commit()


