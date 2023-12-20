#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchmey.ext.declarative import declarative_base
from sqlalchmey import Integer, Column, String, DateTime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, defaulte(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, defaulte(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items() and key not in ('updated_at', 'created_at'):
                if hasattr(self, key):
                    setattr(self, key, value)

            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """delete object"""
        from models import storage
        storage.delete(self)