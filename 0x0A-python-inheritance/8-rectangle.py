#!/usr/bin/python3
"""Empty class"""


class BaseGeometry:
    """raise exception"""

    def area(self):
        """raise alarm"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """inter validator"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value

"""New class to do inhericance"""


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """instatia"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
