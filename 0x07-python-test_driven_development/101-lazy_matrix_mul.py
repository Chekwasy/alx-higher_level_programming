#!/usr/bin/python3
"""module"""


from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrix
    """
    return matmul(m_a, m_b)
