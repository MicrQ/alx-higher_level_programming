#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int): Defaults to 0.
            height (int): Defaults to 0.
        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
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

    def area(self):
        """computes the area"""
        return self.__height * self.__width

    def perimeter(self):
        """computes the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """string representation of the instance"""
        rect = ""
        if self.__height != 0 and self.__width != 0:
            for clm in range(self.__height):
                for row in range(self.__width):
                    rect += str(self.print_symbol)
                if clm != self.__height - 1:
                    rect += "\n"
        return rect

    def __repr__(self):
        """string representation for developer"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """destructor"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares two different rectangles"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2
    
    @classmethod
    def square(cls, size=0):
        """to create new rectangle instance with size * size"""
        return Rectangle(size, size)
