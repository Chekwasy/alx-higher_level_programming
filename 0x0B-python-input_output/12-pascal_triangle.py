#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """function begins"""

    sub = []
    tri = []

    if type(n) is not int:
        return tri

    for a in range(n):
        new = sub[:]
        new.append(1)
        d = len(sub)
        for b in range(1, d):
            new[b] = sub[b - 1] + sub[b]

        sub = new[:]
        tri.append(sub)
    return tri
