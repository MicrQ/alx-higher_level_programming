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
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        return (self.__size ** 2)

    @property
    def size(self):
        """To retrive the value of __size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """To set the value of the __size
        Argumenst:
            size (int): the size of the square
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """prints # size by size"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
