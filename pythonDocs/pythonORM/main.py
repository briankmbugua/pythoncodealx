#creating a database schema
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from datetime import datetime


connection_string = 'mysql+pymysql://root:password@127.0.0.1:3306/sqlAlchemydb'

Base = declarative_base()

engine=create_engine(connection_string, echo=True)


"""
class User
    id int
    username str
    email str
    date_created datetime
"""

class User(Base):
    __tablename__ = 'users'
    #primary key
    id = Column(Integer(), primary_key=True)
    username=Column(String(25),nullable=False,unique=True)
    email=Column(String(88), unique=True,nullable=False)
    date_created=Column(DateTime(), default=datetime.utcnow)

    #return string representation of this object
    def __repr__(self):
        return f"<User username={self.username} email={self.email}>"


new_user=User(id=1,username="Jonathan",email="jona@email.com")
print(new_user)