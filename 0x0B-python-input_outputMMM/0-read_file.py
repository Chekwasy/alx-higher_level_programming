#!/usr/bin/python3
"""function to readfile"""


def read_file(filename=""):
    """funct"""

    with open(filename, "r", encoding="utf-8") as file1:
        txt = file1.read()
        print(txt, end='')
