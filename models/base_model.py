#!/usr/bin/python3
"""This class defines all common attributes/methods for \
other classes """


import uuid
from .__init__ import storage
from datetime import datetime


class BaseModel:
    """This class defines all common attributes/methods for \
other classes"""
    def __init__(self, *args, **kwargs):
        """instantiation with id, and datetime for creation and update"""
        if kwargs:
            for (key, value) in kwargs.items():
                if key == "__class__":
                    pass
                if key == "created_at":
                    self.created_at = datetime.fromisoformat(value)
                if key == "updated_at":
                    self.updated_at = datetime.fromisoformat(value)
                if key == "id":
                    self.id = str(value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            storage.new(self)

    def __str__(self):
        """returns class name, id, and dictionary"""
        return("[{}] ({}) {}".format(str(self.__class__.__name__),\
               str(self.id), self.__dict__))

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__
        new_dict.update(__class__=str(self.__class__.__name__))
        new_dict.update(created_at=datetime.isoformat(self.created_at))
        new_dict.update(updated_at=datetime.isoformat(self.updated_at))
        return new_dict
