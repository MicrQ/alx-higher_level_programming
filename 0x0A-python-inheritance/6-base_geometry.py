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
