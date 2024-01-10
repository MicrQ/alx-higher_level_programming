#!/usr/bin/python3
"""student class"""


class Student:
    """represents student"""

    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to retrive a dictiionary representation"""
        return self.__dict__
