#!/usr/bin/python3
"""Prints the State object with the name passed as argument from the database"""
from engine2 import engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name == sys.argv[4])
    try:
        print(results[0].id)
    except IndexError:
        print("Not found")

