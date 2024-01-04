#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """ Initialization of the rextangle

        Args:
            width (int): Defaults to 0.
            height (int): Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set the width

        Args:
            value (int): the new width

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an intege")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To retrive the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set the value of height

        Args:
            value (int): the new value of height

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
