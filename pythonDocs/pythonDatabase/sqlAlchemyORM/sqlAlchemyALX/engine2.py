#!/usr/bin/python3
from sqlalchemy import create_engine

engine = create_engine('mysql+://root:password@localhost:3306/onedb', echo=True, pool_pre_ping=True)

print(engine)