#!/usr/bin/python3
"""function to replace a string after a line another string is found"""


def append_after(filename="", search_string="", new_string=""):
    """the func begins"""

    with open(filename, "r", encoding="utf-8") as file1:
        txt = file1.readlines()
        lst = []
        for lines in txt:
            lst.append(lines)
            if search_string in lines:
                lst.append(new_string)
    with open(filename, "w", encoding="utf-8") as file2:
        for ln in lst:
            file2.write(ln)
