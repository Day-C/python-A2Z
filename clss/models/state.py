#!/usr/bin/python3
'''State class'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class State(BaseModel, Base):
    '''State inherits the base model.'''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
