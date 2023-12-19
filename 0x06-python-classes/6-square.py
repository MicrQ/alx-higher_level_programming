#!/usr/bin/python3
"""Difines a square"""


class Square:
    """Elements as follow"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes size if given

        Argumenst:
            size (int): the size of the square
            position (tuple): position on the square
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
            self.__position = position
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

    @property
    def position(self):
        """To retrive position"""
        return (self.__position)

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

    @position.setter
    def position(self, value):
        """Position setter"""
        if type(value) != int or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints # size by size"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            if self.__position[1] <= 1:
                for p in range(self.__position[0]):
                    print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
