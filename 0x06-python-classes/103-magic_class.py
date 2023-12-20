#!/usr/bin/python3
""" Magic class """

import math


class MagicClass:
    """Circle"""

    def __init__(self, radius=0):
        """Initializes radius
        Arg:
            radius(int or float): radius of the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Computes the area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """circumference computer"""
        return (2 * math.pi * self.__radius)
