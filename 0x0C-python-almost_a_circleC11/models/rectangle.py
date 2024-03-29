#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """The class"""

    @property
    def width(self):
        """width property"""

        return self.__width

    @width.setter
    def width(self, width):
        """set width"""

        self.chkval(width, "width")
        self.__width = width

    @property
    def height(self):
        """height property"""

        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""

        self.chkval(height, "height")
        self.__height = height

    def chkval(self, val, strr):
        """chkval setter"""

        if type(val) is not int:
            raise TypeError(strr + " must be an integer")
        elif val <= 0 and (strr == "width" or strr == "height"):
            raise ValueError(strr + " must be > 0")
        elif val < 0 and (strr == "x" or strr == "y"):
            raise ValueError(strr + " must be >= 0")

    @property
    def x(self):
        """x property"""

        return self.__x

    @x.setter
    def x(self, x):
        """set x"""

        self.chkval(x, "x")
        self.__x = x

    @property
    def y(self):
        """y property"""

        return self.__y

    @y.setter
    def y(self, y):
        """set y"""

        self.chkval(y, "y")
        self.__y = y

    def area(self):
        """area of rectangle"""

        self.area = (self.__width * self.__height)
        return self.area

    def display(self):
        """Display"""

        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """str representation"""

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """args stuff"""

        argc = len(args)
        kwarg = len(kwargs)
        if argc > 5:
            argc = 5
        atr = ["id", "width", "height", "x", "y"]
        if argc > 0:
            for i in range(argc):
                setattr(self, atr[i], args[i])
        elif kwarg > 0:
            for j, k in kwargs.items():
                if j in atr:
                    setattr(self, j, k)

    def __init__(self, width, height, x=0, y=0, id=None):
        """init for rectangle class"""

        self.chkval(width, "width")
        self.chkval(height, "height")
        self.chkval(x, "x")
        self.chkval(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.area
        self.display
        super().__init__(id)

    def to_dictionary(self):
        """
        ...
        """

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
