#!/usr/bin/python3
from model_state import Base
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
        engine = create_engine('mysql+pymysql://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True, echo=True)
        Base.metadata.create_all(engine)
