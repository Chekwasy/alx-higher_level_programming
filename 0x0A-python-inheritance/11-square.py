#!/usr/bin/python3
"""Square Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class begins"""

    def __init__(self, size):
        """init method"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area method"""

        return self.__size * self.__size

    def __str__(self):
        """str method"""

        return "[Square] " + str(self.__size) + "/" + str(self.__size)
