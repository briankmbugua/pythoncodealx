#!/usr/bin/python3

from engine2 import engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State


if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State.name, City.id, City.name).filter(State.id == City.state_id)
    for result in results:
         print(f"{result[0]}: ({str(result[1])}) {result[2]}")

