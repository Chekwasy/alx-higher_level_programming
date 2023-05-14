#!/usr/bin/python3
"""adding module"""


def add_integer(a, b=98):
    """Adding two int numbeea"""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    result = float(a) + float(b)
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if result == float('inf') or result == -float('inf'):
        return "inf"
    return (a + b)
