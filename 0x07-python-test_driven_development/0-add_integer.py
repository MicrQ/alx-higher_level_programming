#!/usr/bin/python3
"""Defining add_integer function"""


def add_integer(a, b=98):
    """_summary_

    Args:
        a (int): first argument
        b (int, optional): second argument. Defaults to 98.

    Raises:
        TypeError: if not integer or float
        TypeError: if not integer or float

    Returns:
        int: the addition of two numbers
    """
    msg = " must be an integer"
    if type(a) is not int and type(a) is not float:
        raise TypeError("a" + msg)
    if type(b) is not int and type(b) is not float:
        raise TypeError("b" + msg)
    return int(a) + int(b)
