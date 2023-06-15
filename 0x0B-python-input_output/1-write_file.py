#!/usr/bin/python3
"""function to write file"""


def write_file(filename="", text=""):
    """the func"""

    with open(filename, "w", encoding="utf-8") as file1:
        nb = file1.write(text)
        return nb
