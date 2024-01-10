#!/usr/bin/python3
"""say_my_name function"""


def say_my_name(firstname, lastname=""):
    """printin fullname"""
    if not isinstance(firstname, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(lastname, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(firstname, lastname))
