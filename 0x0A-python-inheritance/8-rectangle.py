#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Empty class"""


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """instatia"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
