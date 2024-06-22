#!/usr/bin/python3
'''State class'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class State(BaseModel):
    '''State inherits the base model.'''

    name = Column(string)128), nullable=False)
