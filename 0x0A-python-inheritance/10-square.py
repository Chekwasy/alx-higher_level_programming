#!/usr/bin/python3
"""Square Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class begins"""

    def __init__(self, size):
        """init method"""

        super().__init__(size,size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area method"""

        return self.__size * self.__size
