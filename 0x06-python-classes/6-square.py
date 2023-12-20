#!/usr/bin/python3
"""Difines a square"""


class Square:
    """Elements as follow"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes size if given

        Argumenst:
            size (int): the size of the square
            position (int, int): position on the square
        """
        self.size = size
        self.position = position

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
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """To retrive position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Position setter"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(j >= 0 for j in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints # size by size"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[1] <= 1:
                    for p in range(self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
