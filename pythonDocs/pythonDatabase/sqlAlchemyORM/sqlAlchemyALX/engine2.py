#!/usr/bin/python3
from sqlalchemy import create_engine
import sys
engine = create_engine('mysql+pymysql://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]), echo=True, pool_pre_ping=True)

