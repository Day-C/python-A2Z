#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = 'first'
print(my_model)
jsoned = my_model.to_dict()
print(jsoned)
'''
for key in jsoned.keys():
        print("\t{}: ({}) - {}".format(key, type(jsoned[key]), jsoned[key]))
'''
print("--------\n--------")
new_models = BaseModel(**jsoned)

