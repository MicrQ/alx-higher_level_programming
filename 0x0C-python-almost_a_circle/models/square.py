#!/usr/bin/python3
"""the square class"""


from models.rectangle import Rectangle


"""importing Rectangle class"""


class Square(Rectangle):
    """Represents Square, Rectangle, Base classes"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the Square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """taking unspecified arguments.
            args: high priority
            kwargs: if len(args) == 0
        """
        if args and len(args) != 0:
            count = 0
            for value in args:
                if count == 0:
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif count == 1:
                    self.size = value
                elif count == 2:
                    self.x = value
                elif count == 3:
                    self.y = value
                count += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
