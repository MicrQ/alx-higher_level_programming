#!/usr/bin/python3
"""defining add_attribute function"""


def add_attribute(obj, name, value):
    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
