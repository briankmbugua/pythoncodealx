#!/usr/bin/python3
import uuid
from datetime import datetime
import json

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(kwargs['created_at'],'%Y-%m-%dT%H:%M:%S.%f')
        if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        # Save the changes to the file
        from models.engine import storage # lazy import to solve a circular import issue
        storage.new(self)
        storage.save()
    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        self.updated_at = datetime.now()
        # Save the changes to the file
        from models.engine import storage
        storage.save()
    
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = BaseModel.__name__
        return obj_dict
    
    @classmethod
    def from_dict(cls, d):
        return cls(**d)
    

# newModel = BaseModel()


with open('data.json', 'a') as file:
    newModel3 = BaseModel()
    new_dict = newModel3.to_dict()
    json.dump(new_dict, file)
    file.write('\n')
with open('data.json', 'a') as file:
    newModel4 = BaseModel()
    new_dict = newModel4.to_dict()
    json.dump(new_dict, file)
    file.write('\n')
with open('data.json', 'a') as file:
    newModel5 = BaseModel()
    new_dict = newModel5.to_dict()
    json.dump(new_dict, file)
    file.write('\n')
with open('data.json', 'a') as file:
    newModel6 = BaseModel()
    new_dict = newModel6.to_dict()
    json.dump(new_dict, file)
    file.write('\n')

with open('data.json', 'r') as file:
    obj_dict = json.load(file)
    print(obj_dict)

