#!/usr/bin/python3
"""module
"""


def check_matrix(matrix, name):
    """matrix multiply """

    if type(matrix) is list:
        if len(matrix) == 0:
            raise ValueError(name + " can't be empty")
        for row in matrix:
            if type(row) is list:
                if len(row) == 0:
                    raise ValueError(name + " can't be empty")
                else:
                    for ele in row:
                        if type(ele) not in [int, float]:
                            raise TypeError(name + " should contain only" +
                                            " integers or floats")
            elif type(row) is not list:
                raise TypeError(name + " must be a list of lists")
            elif len(row) == 0:
                raise ValueError(name + " can't be empty")
            if len(row) != len(matrix[0]):
                raise TypeError("each row of " + name + " must be of the" +
                                " same size")
    else:
        raise TypeError(name + " must be a list")


def matrix_mul(m_a, m_b):
    """
        Multiply two matrix
    """

    check_matrix(m_a, 'm_a')
    check_matrix(m_b, 'm_b')
    cols_a = len(m_a[0])
    rows_b = len(m_b)

    if cols_a == rows_b:
        rows = len(m_a)
        cols = len(m_b[0])
        result = []
        for i in range(rows):
            fil = []
            for j in range(cols):
                fil.append(0)
            result.append(fil)
        for i in range(len(m_a)):
            for j in range(len(m_b[0])):
                for k in range(len(m_b)):
                    result[i][j] += m_a[i][k] * m_b[k][j]
        return result
    else:
        raise ValueError("m_a and m_b can't be multiplied")
