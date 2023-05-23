#!/usr/bin/python3
"""
Contains class defination of a state and an instane Base = declarative_base();
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# state table

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)


"""
EXPLANATION FOR THE ABOVE CODE
First we import classes necessary to create a table Column, Integer, String
Column -- this is provided by SQLAlchemy and represents a column in a database table, it is used to define columns and their properties such as data type, constraints, and attributes
##syntax
Column(type, **kwargs)
type -- The type argument specifies the data type of the column it can be any valid SQLAlchemy data type such as Integer, String, Boolean, DateTime

**kwargs -- allows you to provide additional keyword arguments to configure the columns properties this keyword arguments are optional and can be used to specify constraints, attributes, and other properties.Some commonly used keyword arguments include autoincrement, unique, nullable, primary_key

Interger -- this is datatype class provided by SQLAlchemy that represents an interger column in a database table, it is used to define columns that store interger values
String -- Also a datatype class provide by SQLAlchemy that represents a string column in a databse table


##BASE
The base class ('Base') is a class provided by the 'declarative_base()' function.It serves as the base or parent class for all your SQLAlchemy models.When you define your models, they should inherit from this base class.
1.The base class acts as the common ancestor for all your SQLAlchemy models.By inheriting from the base class your models share common functionality and features defined by the base class.
2.Represents the ORM Framework. it provides a set of tools and features that simplify the process of mapping python classes to database tables
3.Metadata storage - the base class holds a special attribute called 'metadata' which stores metadata about your models and their corresponding database tables.Metadata includes information such as tables names, column definations and relationships.
4.Table Creation.The base class provides a convinient method called create_all() that can be used to create all the tables defined by your models.By invoking Base.metadata.create_all(engine)
5.Common Methods and Attributes - the base class may also provide common methods and attributes that are inherited by your models.These methods and attributes can be used for querying, relationship management and other ORM operations.
"""
