#!/usr/bin/python3
"""a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents square"""

    def __init__(self, size):
        """Initialization"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """computes the area"""
        return self.__size ** 2

    def __str__(self):
        """str representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
