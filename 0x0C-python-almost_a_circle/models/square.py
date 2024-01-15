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
