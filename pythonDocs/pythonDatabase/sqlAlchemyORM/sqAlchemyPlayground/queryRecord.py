from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Customers
engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/dbthree', echo=True)

Session = sessionmaker(bind = engine)
session = Session()
result = session.query(Customers).all()
for row in result:
    print("Name: ", row.name, "Address:",row.address, "Email:",row.email)
