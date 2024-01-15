#!/usr/bin/python3
"""Base class implementation"""


import json


class Base:
    """represents Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to file"""
        fName = cls.__name__ + ".json"
        with open(fName, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                listOfDict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(listOfDict))
