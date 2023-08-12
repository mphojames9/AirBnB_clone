#!/usr/bin/python3
from models.base_model import BaseModel

my_ prototype = BaseModel()
my_ prototype.name = "Holberton"
my_ prototype.my_number = 89
print(my_ prototype.id)
print(my_ prototype)
print(type(my_ prototype.created_at))
print("--")
my_ prototype_json = my_ prototype.to_dict()
print(my_ prototype_json)
print("JSON of my_ prototype:")
for key in my_ prototype_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_ prototype_json[key]),
                                       my_ prototype_json[key]))

        print("--")
        my_new_model = BaseModel(**my_ prototype_json)
        print(my_new_model.id)
        print(my_new_model)
        print(type(my_new_model.created_at))

        print("--")
        print(my_ prototype is my_new_model)
