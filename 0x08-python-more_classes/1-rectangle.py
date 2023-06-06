#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class begins"""

    def __init__(self, width=0, height=0):
        """instiation for rectangle"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width getter"""

        return self.width

    @property
    def height(self):
        """Height getter"""

        return self.height

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        """height setter"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
