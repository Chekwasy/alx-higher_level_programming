#!/usr/bin/python3
"""Square class"""


class Square:
    """Square Class
    A Square Class    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__
        The __init__ method initializes the size value of the square.
        Attributes:
            size (:obj:`int`, optional): The size of the square.
        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        if self.__check_tuple(position) is False \
           or self.__check_indexes(position) is False \
           or self.__check_integers(position) is False \
           or self.__check_values(position) is False:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.size = size
        self.position = position

    @property
    def size(self):
        """size property"""

        return self.__size

    @size.setter
    def size(self, size):
        """__init__
        The size setter method update the size value of the square.
        Attributes:
            size (:obj:`int`): The new size of the square.
        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def position(self):
        """position property"""

        return self.__position

    @position.setter
    def position(self, position):
        """position setter"""

        if self.__check_tuple(position) is False \
           or self.__check_indexes(position) is False \
           or self.__check_integers(position) is False \
           or self.__check_values(position) is False:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def __check_tuple(self, position):
        """check tuple"""

        if type(position) is tuple:
            return True

        return False

    def __check_indexes(self, position):
        """check indexes"""

        if len(position) == 2:
            return True

        return False

    def __check_integers(self, position):
        """check integer"""

        if type(position[0]) is int and type(position[1]) is int:
            return True

        return False

    def __check_values(self, position):
        """check values"""

        if position[0] >= 0 and position[1] >= 0:
            return True

        return False

    def area(self):
        """Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """my_print"""

        if self.__size == 0:
            print()
            return None

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')

        a = 0
        b = (self.__position[0])
        for j in range(self.__size):
            for k in range(self.__size):
                if k < self.__position[0] and a == 0:
                    for i in range(b):
                        print(" ", end='')
                a = 1
                print('#', end='')
            print()
            a = 0

    def __str__(self):
        """str rep"""

        dstr = ""
        if self.__size == 0:
            dstr = "\n"
            return dstr

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                dstr = dstr + "\n"
        a = 0
        b = (self.__position[0])
        for j in range(self.__size):
            for k in range(self.__size):
                if k < self.__position[0] and a == 0:
                    for i in range(b):
                        dstr = dstr + " "
                a = 1
                dstr = dstr + "#"
            if j != (self.__size - 1):
                dstr = dstr + "\n"
            a = 0
        return dstr
