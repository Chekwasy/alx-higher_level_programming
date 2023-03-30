#!/usr/bin/python3
"""Class of square"""


class Square:
    """Square Class
    A Square Class
    """

    def __init__(self, size=0):
        """__init__
        The __init__ method initializes the size value of the square.
        Attributes:
            size (:obj:`int`, optional): The size of the square.
        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the current square area
        """

        return self.__size ** 2
