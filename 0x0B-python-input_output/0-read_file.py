#!/usr/bin/python3
"""reading q file"""


def read_file(filename=""):
    """The open function"""

    with open(filename, encoding="utf-8") as a_file:
        for ln in a_file:
            print(ln, end='')
