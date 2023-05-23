#!/usr/bin/python3
"""
Contains the class defination of a State and an instance Base = declarative_base();
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# state
class State(Base):
    __tablename = 'state'
    """
    state class inherits from base links to MySQL table states
    class attribute id auto_generated, unique interger,can't be null and is primary key
    """
    id = Column(Integer(), autoincrement=True,unique=True,primary_key=True,nullable=False)
    name = Column(String(128), nullable=False)