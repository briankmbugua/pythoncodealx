#!/usr/bin/python3
from models.engine import storage
from models.base_model import BaseModel

all_objs = storage.all()

print(all_objs)
