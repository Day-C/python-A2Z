#!/usr/bin/python3
'''make models a module'''
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
