#!/usr/bin/python3
"""defining instance checker class"""


def is_kind_of_class(obj, a_class):
    """returns true if obj is instance of a_class

    Args:
        obj : object
        a_class: class to check
    """
    return isinstance(obj, a_class)
