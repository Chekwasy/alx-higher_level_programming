#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class begins"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """instiation for rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

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

    def __str__(self):
        """str method"""

        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i != (self.__height - 1):
                string += "\n"
        return string

    def __repr__(self):
        """rep method"""

        return "Rectangle("+str(self.__width)+", "+str(self.__height)+")"

    def __del__(self):
        """delte method"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method to check bigger rectangle"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method to return square instance of the rectangle class"""

        return Rectangle(size, size)
