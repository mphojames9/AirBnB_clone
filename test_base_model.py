#!/usr/bin/python3
from models.base_model import BaseModel

my_ prototype = BaseModel()
my_ prototype.name = "Holberton"
my_ prototype.my_number = 89
print(my_ prototype)
my_ prototype.save()
print(my_ prototype)
my_ prototype_json = my_ prototype.to_dict()
print(my_ prototype_json)
print("JSON of my_ prototype:")
for key in my_ prototype_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_ prototype_json[key]),
                                   my_ prototype_json[key]))
