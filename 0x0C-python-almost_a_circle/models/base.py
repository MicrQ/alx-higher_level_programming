#!/usr/bin/python3
"""Base class implementation"""


import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """from json string to object creation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns a class object from a dictionary of attribute"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                New = cls(1, 1)
            else:
                New = cls(1)
            New.update(**dictionary)
            return New

    @classmethod
    def load_from_file(cls):
        """Return a list of classes"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                listOfDicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**dic_t) for dic_t in listOfDicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """CSV serialization of a list of objects"""
        fName = cls.__name__ + ".csv"
        with open(fName, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """from a CSV file."""
        fName = cls.__name__ + ".csv"
        try:
            with open(fName, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                listOfDicts = csv.DictReader(csvfile, fieldnames=fields)
                listOfDicts = [dict([k, int(v)] for k, v in d.items())
                               for d in listOfDicts]
                return [cls.create(**d) for d in listOfDicts]
        except IOError:
            return []
