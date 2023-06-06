#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class begins"""

    def __init__(self, width=0, height=0):
        """instiation for rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter"""

        return self.__width

    @property
    def height(self):
        """Height getter"""

        return self.__height

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area method"""

        return self.__width * self.__height

    def perimeter(self):
        """primeter method"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + (2 * self.__height)
