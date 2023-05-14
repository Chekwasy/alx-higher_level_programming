#!/usr/bin/python3
"""Matix divide"""


def matrix_divided(matrix, div):
    """the function for it"""

    a = 0
    b = 0
    _all = []
    _som = []
    if type(matrix) is not list or (len(matrix) == 0) or type(matrix[0])\
       is not list or (len(matrix[0]) == 0):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if div == float('inf') or div == -float('inf') or div != div:
        div = 1
    if div == ((2**1023)+(2**1023)) or div == -((2**1023)+(2**1023)):
        div = 1
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        a = len(i)
        if b != 0 and a != b:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            b = a
            _som.append(round(j / div, 2))
        _all.append(_som)
        _som = []
    return _all
