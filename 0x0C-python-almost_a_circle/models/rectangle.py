#!/usr/bin/python3
"""Rectangle Class which inherit from Base class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class begins"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization stuff"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width method getter"""

        return self.__width

    @width.setter
    def width(self, width):
        """width method setter"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height method getter"""

        return self.__height

    @height.setter
    def height(self, height):
        """height method"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x method setter"""

        return self.__x

    @x.setter
    def x(self, x):
        """x method setter"""

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y method getter"""

        return self.__y

    @y.setter
    def y(self, y):
        """y method setter"""

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Area of rectangle method """

        return (self.__width * self.__height)

    def display(self):
        """display method"""

        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print("")
