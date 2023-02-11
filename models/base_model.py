#!/usr/bin/python3
"""
This module writes a class that
defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ Defines all common attributes/method for other classes """
    def __init__(self, *args, **kwargs):
        """ instatitates public instance attributes """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at":
                    value = datetime.fromisoformat(value)
                if key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ str magic format to return string representation of the class. """
        ids = self.id
        return "[{}] ({}) {}".format(__class__.__name__, ids, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all key/values of __dict__"""
        obj_dict = {}
        obj_dict["__class__"] = f'{self.__class__.__name__}'
        for key, value in self.__dict__.items():
            if key == 'created_at':
                value = (self.created_at).isoformat()
            if key == 'updated_at':
                value = (self.updated_at).isoformat()
            obj_dict[key] = value
        return obj_dict
