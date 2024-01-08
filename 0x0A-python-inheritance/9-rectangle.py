#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents Rectangle"""

    def __init__(self, width, height):
        """Initialization of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """computes the area"""
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
