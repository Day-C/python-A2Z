#!/usr/bin/python3
'''Database storage engine.'''
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from os import getenv


classes = {"User": User, "Place": Place, "City": City, "State": State, "Amenity": Amenity, "Review": Review}


class DBStorage():
    '''database engine.'''

    __session = None
    __engine = None

    def __init__(self):
        '''Initialize instance attributes.'''

        usr = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        hst = 'localhost'
        dbs = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(usr, pwd, hst, dbs))


        if getenv('HBNB_ENV')== 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''query the current session for all cls objects or all objects.'''

        all_cls = {}
        if cls != None and cls in classes:
           all_cls = self.__session.query(classes[cls]).all()
        else:
            for clss in classes:
                all_cls = self.__session.query(classes[clss]).all()
        all_objs = {}
        for obj in all_cls:
            key = obj.__class__.__name__ + "." + obj.id
            all_objs[key] = obj

        return (all_objs)

    def new(self, obj):
        '''Add an object to the current session.'''

        self.__session.add(obj)

    def save(self):
        '''Commit all changes of the current session.'''

        self.__session.commit()

    def delete(self, obj=None):
        '''Delete obj from the current database session.'''

        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        '''Create all tables in the database.'''

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=True)
        Session = scoped_session(session_factory)
        self.__session = Session

