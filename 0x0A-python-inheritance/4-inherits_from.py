#!/usr/bin/python3
"""defining inherits_from function"""


def inherits_from(obj, a_class):
    """returns true if obj is subclass of a_class

    Args:
        obj : subclass
        a_class :superclass
    """
    return isinstance(obj, a_class) and type(obj) != a_class
