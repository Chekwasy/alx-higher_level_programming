#!/usr/bin/python3
"""A Program that define rectangle"""


class Rectangle:
    """Class Instance definition"""

    def __init__(self, width=0, height=0):
        """init initialization"""

        self.width = width
        self.height = height

    """Class attribute width"""

    @property
    def width(self):
        """Property width"""

        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Another Class atrribute"""

    @property
    def height(self):
        """height property"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
