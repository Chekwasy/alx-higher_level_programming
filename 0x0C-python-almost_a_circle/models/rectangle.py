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

        self.__width = width

    @property
    def height(self):
        """height method getter"""

        return self.__height

    @height.setter
    def height(self, height):
        """height method"""

        self.__height = height

    @property
    def x(self):
        """x method setter"""

        return self.__x

    @x.setter
    def x(self, x):
        """x method setter"""

        self.__x = x

    @property
    def y(self):
        """y method getter"""

        return self.__y

    @y.setter
    def y(self, y):
        """y method setter"""

        self.__y = y
