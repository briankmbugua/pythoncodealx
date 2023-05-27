#!/usr/bin/python3
from engine import engine

#   Another way to make table objects, This section will illustrate the same Table metadata of the previous sections being constructed using Declarative Table.When using ORM, the process by which we declare Table metadata is usually combined with the process of declaring mapped classes.The mapped class is any Python class we'd like to create which will then have attributes on it that will be linked to the columns in a database table.The most common style is known as declarative and allows us to declare our user_defined classes and metadata at once.
# ESTABLISHING A DECLARATIVE BASE
#The most expedient way to acquire a new Declarative Base is to create a new class that subclasses the SQLAlchemy DeclarativeBase class:

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
# Above, the Base class is what we'll refer towards as the Declarative Base.When we make new classes that are subclasses of Base, combined with appropriate class-level directives they will each be described as a new ORM mapped class at class creation time.each one typically but not exclusively reffering to a particular table.The Declarative base refers to a MetaData collection that is created for us automatically.It is accesible via the DeclarativeBase.metadata class level attribute.As we create new mapped classes, they each will reference a Table within this MetaData collection.

print(Base.metadata)

# A set of of ORM mapped classes will coordinate with each other via registry.The Declarative Base refers to this registry which we can acces via the DeclarativeBase.registry

print(Base.registry)

# DECLARING MAPPED Classes
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import ForeignKey

class User(Base):
    __tablename__ = "user_account"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name = {self.name!r}, fullname = {self.fullname!r})"



class Addres(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))
    user: Mapped[User] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id = {self.id!r}, email_address={self.email_address!r})"

