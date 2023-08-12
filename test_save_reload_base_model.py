#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_ prototype = BaseModel()
my_ prototype.name = "Holberton"
my_ prototype.my_number = 89
my_ prototype.save()
print(my_ prototype)
