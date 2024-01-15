#!/usr/bin/python3
"""making it executable"""

from models.base import Base
"""Importing the Base class"""


class Rectangle(Base):
    """Represents rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """to compute the area of the rectangle object"""
        return self.__width * self.__height

    def display(self):
        """displays the rectangle using #"""
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """__str__ to return [Rectangle] (id) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """updates given arguments to attributes
        args: order is important
            1st: id, 2nd: width, 3rd: height, 4th: x, 5th: y
        kwargs: no order needed(key/value pair)
            """
        if len(args) > 0:
            i = 0
            for value in args:
                if i == 0:
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif i == 1:
                    self.width = value
                elif i == 2:
                    self.height = value
                elif i == 3:
                    self.x = value
                elif i == 4:
                    self.y = value
                else:
                    break
                i += 1
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
