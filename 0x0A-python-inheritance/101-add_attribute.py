#!/usr/bin/python3
"""defining add_attribute function"""


def add_attribute(obj, name, value):
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
