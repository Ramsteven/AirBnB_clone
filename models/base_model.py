#!/usr/bin/python3
""" BaseModel class """
from datetime import datetime
import models
import uuid


class BaseModel:
    """ Init method  """
    def __init__(self, *args, **kwargs):
        """ init method """
        if kwargs is None or len(kwargs) < 1:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
            self.created_at = datetime.fromisoformat(
                                                     kwargs["created_at"])
            self.updated_at = datetime.fromisoformat(
                                                     kwargs["updated_at"])

    def __str__(self,):
        """ str method  """
        x = "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
        return x

    def save(self):
        """ save method  """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to dict method method to dictionary data """
        dic_n = self.__dict__.copy()
        if 'created_at' in dic_n:
            dic_n['created_at'] = (
                                   dic_n['created_at']).isoformat()
        if 'updated_at' in dic_n:
            dic_n['updated_at'] = (
                                   dic_n['updated_at']).isoformat()
        dic_n['__class__'] = self.__class__.__name__
        return dic_n
