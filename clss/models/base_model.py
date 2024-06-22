#!/usr/bin/python3
'''Shop class'''
from sqlalchemy.declarative import declarative_base
from sqlalchemy import Column, String, Ingeter, DateTime
from datetime import datetime
import models
import uuid

Base = declarative_base()


class BaseModel():
    '''Mother class.'''

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(dateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        # Hadle creating a base model from a dictionary 
        if kwargs:
            format = '%Y-%m-%dT%H:%M:%S.%f'
            for key in kwargs.keys():
                if key != '__class__':
                    setattr(self, key, kwargs[key])
            if kwargs.get('created_at', None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(self.created_at, format)
            else:
                self.created_at = datetime.now()
            if kwargs.get('updated_at', None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(self.updated_at, format)
            else:
                updated_at = datetime.now()
            if kwargs.get('id', None) is None:
                self.id = str(uuid.uuid4())

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()


    def __str__(self):
        '''display class information.'''

        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        '''update the 'updated_at' instance attribute.'''

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''Create a dictionary of all instances.'''
        
        new_dict = self.__dict__
        #convert date and time values to sting
        new_dict['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        new_dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)



