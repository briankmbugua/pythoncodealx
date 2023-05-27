#!/usr/bin/python3
from engine2 import engine
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name.like('%a%'))
    for result in results:
        session.delete(result)
    session.commit()

