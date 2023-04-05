#!/usr/bin/python3
def matrix_divided(matrix, div):
    a = 0
    b = 0
    if len(matrix) < 1:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if div is not int and div is not float:
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
            if type(j) is not int or type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            b = a
