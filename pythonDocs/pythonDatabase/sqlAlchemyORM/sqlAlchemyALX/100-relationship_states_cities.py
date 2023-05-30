#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from engine2 import engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()
