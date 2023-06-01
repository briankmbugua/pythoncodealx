#!/usr/bin/python3

import json

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file into instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(new_dict, file)
    
    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file(__file_path) exists)"""
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
                class_obj = eval(class_name)
                self.__objects[key] = class_obj(**value)
        except FileNotFoundError:
            pass
