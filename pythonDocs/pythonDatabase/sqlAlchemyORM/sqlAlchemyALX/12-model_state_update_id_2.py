#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa
Change the name of the State where id = 2 to New Mexico"""
from engine2 import engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter_by(id=2).first()
    results.name = "New Mexico"
    session.commit()
