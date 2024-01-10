#!/usr/bin/python3
"""student class"""


class Student:
    """represents student"""

    def __init__(self, first_name, last_name, age):
        """Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to retrive a dictiionary representation"""
        if attrs is None:
            return self.__dict__

        new_dict = {}
        # for item in attrs:
        #     try:
        #         new_dict[item] = self.__dict__[item]
        #     except Exception:
        #         pass
        for item in attrs:
            if item in self.__dict__.keys():
                new_dict[item] = self.__dict__[item]
        return new_dict
