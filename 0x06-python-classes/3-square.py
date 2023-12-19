#!/usr/bin/python3
"""Difines a square"""


class Square:
    """Elements as follow"""

    def __init__(self, size=0):
        """Initializes size if given

        Argumenst:
            size (int): the size of the square
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the area of the square
        """
        return (self.__size * self.__size)
