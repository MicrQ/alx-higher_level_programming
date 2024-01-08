#!/usr/bin/python3
"""defining is_same_class_ finction"""


def is_same_class(obj, a_class):
    """returns true if obj is instance of a_class

    Args:
        obj: object to be checked
        a_class: the class
    """
    return type(obj) is a_class
