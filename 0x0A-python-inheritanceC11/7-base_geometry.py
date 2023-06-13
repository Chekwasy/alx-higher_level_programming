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
