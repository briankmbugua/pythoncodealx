#!/usr/bin/python3
"""
Contains class defination of a state and an instane Base = declarative_base();
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# state table

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
