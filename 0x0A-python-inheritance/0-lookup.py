#!/usr/bin/python3
"""Defining lookup function"""


def lookup(obj):
    """Return a list of all attributes of obj
    Args:
        obj: object
    """
    return dir(obj)
