#!/usr/bin/python3
"""A Program that define rectangle"""


class Rectangle:
    """Class Instance definition"""

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """init initialization"""

        type(self).number_of_instances += 1
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

    """ Area of Rectangle public insyance method"""

    def area(self):
        """Area of rectangle"""

        return self.__width * self.__height

    """ Perimeter public instance methd"""

    def perimeter(self):
        """It beginns"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """string stuff return"""

        if self.__width == 0 or self.__height == 0:
            return ""
        dstr = []
        for i in range(self.__height):
            for j in range(self.__width):
                dstr.append("#")
            if (self.__height - 1) is not i:
                dstr.append("\n")
        return "".join(dstr)

    def __repr__(self):
        """Return the string representation of the Rectangle."""

        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
