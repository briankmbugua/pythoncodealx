#!/usr/bin/python3
"""A script that adds the State object "Louisiana" to the database hbtn_0e_6_usa"""

from engine2 import engine
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    new_instance = session.query(State).filter_by(name='Lousiana').first()
    session.commit()
