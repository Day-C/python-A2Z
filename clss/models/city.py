#!/usr/bin/python3
'''City class'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    '''city inherits from base model.'''

    __tablename__ = "cities"
    state_id = Column(String(60), nullable=True)
    name = Column(String(128), nullable=False)
