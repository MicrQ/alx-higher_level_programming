#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """returns dictionary of the object"""
    return obj.__dict__
