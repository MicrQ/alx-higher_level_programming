#!/usr/bin/python3
"""defines BaseGeometry class"""


class BaseGeometry:
    """represents a geometry"""
    def area(self):
        """computes area

        Raises:
            Exception: if not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """int validator

        Args:
            name (str): the name
            value (int): the value
        """
        if not type(value) == int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
        
