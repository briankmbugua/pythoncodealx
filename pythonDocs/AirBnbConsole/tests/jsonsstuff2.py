import json
from ..models import base_model
# with open("file.json", "r") as file:
#     data = json.load(file)

# print(data)

# {
#     'BaseModel.00ff08b3-60b1-4596-9902-2bb99053f87d': {'id': '00ff08b3-60b1-4596-9902-2bb99053f87d', 'created_at': '2023-06-01T23:58:44.167674', 'updated_at': '2023-06-01T23:58:44.168006', 'name': 'My_First_Model', 'my_number': 89, '__class__': 'BaseModel'},

#     'BaseModel.fd551b5d-bcea-4e8b-9935-573fcb0e1ab5': {'id': 'fd551b5d-bcea-4e8b-9935-573fcb0e1ab5', 'created_at': '2023-06-02T00:29:20.606894', 'updated_at': '2023-06-02T00:29:20.607377', 'name': 'My_First_Model', 'my_number': 89, '__class__': 'BaseModel'},

#     'BaseModel.ef6a93b1-1f39-4984-80da-a6586fe2742c': {'id': 'ef6a93b1-1f39-4984-80da-a6586fe2742c', 'created_at': '2023-06-02T00:30:55.039577', 'updated_at': '2023-06-02T00:30:55.040438', 'name': 'My_Second_Model', 'my_number': 90, '__class__': 'BaseModel'}
# }


with open("file.json", "r") as file:
    obj_dict = json.load(file)
    for key, value in obj_dict.items():
        class_name, obj_id = key.split('.')
        print(class_name)
        print(obj_id)

print(obj_dict)

emptydict = {}

for key, value in obj_dict.items():
    class_name, obj_id = key.split('.')
    class_obj = eval(class_name)
    emptydict[key] = class_obj(**value)
"""
BaseModel
00ff08b3-60b1-4596-9902-2bb99053f87d
BaseModel
fd551b5d-bcea-4e8b-9935-573fcb0e1ab5
BaseModel
ef6a93b1-1f39-4984-80da-a6586fe2742c
"""
# {
#     'BaseModel.00ff08b3-60b1-4596-9902-2bb99053f87d': {'id': '00ff08b3-60b1-4596-9902-2bb99053f87d', 'created_at': '2023-06-01T23:58:44.167674', 'updated_at': '2023-06-01T23:58:44.168006', 'name': 'My_First_Model', 'my_number': 89, '__class__': 'BaseModel'},
#     'BaseModel.fd551b5d-bcea-4e8b-9935-573fcb0e1ab5': {'id': 'fd551b5d-bcea-4e8b-9935-573fcb0e1ab5', 'created_at': '2023-06-02T00:29:20.606894', 'updated_at': '2023-06-02T00:29:20.607377', 'name': 'My_First_Model', 'my_number': 89, '__class__': 'BaseModel'},
#     'BaseModel.ef6a93b1-1f39-4984-80da-a6586fe2742c': {'id': 'ef6a93b1-1f39-4984-80da-a6586fe2742c', 'created_at': '2023-06-02T00:30:55.039577', 'updated_at': '2023-06-02T00:30:55.040438', 'name': 'My_Second_Model', 'my_number': 90, '__class__': 'BaseModel'}
# }
