#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from engine2 import engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(f"{instance.id}: {instance.name}")
