#!/usr/bin/python3
'''Handle file stograge.'''
import json
from models.base_model import BaseModel


class FileStorage():
    '''serialize and dezerialize to and from a json file.'''

    __file_path = 'file.json'
    __objects = {}




    def all(self):
        '''Return the dictonary objects.'''

        if self.reload():
            return self.reload()
        return {}

    def new(self, obj):
        '''create a key for the object.'''
        # sets in __objects the obj with key <obj class name>.id

        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj.__dict__

    def save(self):
        '''Serialize object to Json file'''
        
        all_objects = self.all()
        # add the new object into dic containing older objects
        
        for key in self.__objects.keys():
            all_objects[key] = self.__objects[key]

        print(type(all_objects))
        with open(self.__file_path, 'w') as f:
            # write the class dict into file and convert datetime to string
            f.write(json.dumps(all_objects, default=str))
 
    def reload(self):
        '''deserialize json file to object.'''

        try:
            with open(self.__file_path, 'r') as f:
                data = f.read()
                if len(data) == 0:
                    return {}
                return json.loads(data)
        except FileNotFoundError:
            pass
