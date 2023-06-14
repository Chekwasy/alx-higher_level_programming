#!/usr/bin/python3
"""function to append file"""


def append_write(filename="", text=""):
    """the func"""

    with open(filename, "a", encoding="utf-8") as file1:
        nb = file1.write(text)
        return nb
