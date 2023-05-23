from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine('pymsql+mysql://root:password@127.0.0.1:3306/threedb', echo = True)

session = sessionmaker()

session(bind=engine)
