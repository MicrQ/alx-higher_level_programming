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
        """int validator"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
