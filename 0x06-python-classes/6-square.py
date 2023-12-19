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
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of the square
        """
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
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

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

    @property
    def position(self):
        """To retrive position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
