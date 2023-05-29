#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square begins"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization for square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation method for square"""

        return "[Square] "+"("+str(self.id)+") "+str(self.x)+"/" \
            + str(self.y)+" - "+str(self.width)

    @property
    def size(self):
        """size getter method"""

        return self.width

    @size.setter
    def size(self, size):
        """size setter method"""

        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size

    def update(self, *args, **kwargs):
        """Update method for args and kwargs"""

        ln = len(args)
        if ln > 5:
            ln = 5
        lst = ["id", "size", "x", "y"]
        if ln > 0:
            for i in range(ln):
                setattr(self, lst[i], args[i])
        else:
            for i, j in kwargs.items():
                if hasattr(self, i):
                    setattr(self, i, j)
