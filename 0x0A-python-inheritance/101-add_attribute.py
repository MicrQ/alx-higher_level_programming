#!/usr/bin/python3
"""defining add_attribute function"""


def add_attribute(obj, name, value):
    """adds a new attribute if possible

    Args:
        obj (object): to add new attribute
        name (any): key
        value (any): value

    Raises:
        TypeError: can't add new attribute
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
