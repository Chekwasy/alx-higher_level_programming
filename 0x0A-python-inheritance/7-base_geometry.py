#!/usr/bin/python3
"""Basegeometry class"""


class BaseGeometry:
    """Class begins"""

    def area(self):
        """method for area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator method"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value
