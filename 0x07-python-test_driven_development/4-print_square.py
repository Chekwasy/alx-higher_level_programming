#!/usr/bin/python3
"""module"""


def print_square(size):
    """
    pribt square of #
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#'*size)
