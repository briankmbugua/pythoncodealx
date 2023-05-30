#!/usr/bin/python3
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String, ForeignKey
from model_state import Base

class City(Base):
    """The class defination of a city"""
    __tablename__ = 'cities'
    id = Column(autoincrement=True, unique=True, nullable=False,primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
