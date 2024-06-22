#!/usr/bin/python3
'''City class'''
from models.base_model import BaseModel, Base
from sqlalchemy Column, String

class City(BaseModel, Base):
    '''city inherits from base model.'''

    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False)
    name = Column(string(128), nullable=False)
