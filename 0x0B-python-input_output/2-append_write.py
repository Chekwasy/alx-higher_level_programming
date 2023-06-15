#!/usr/bin/python3
"""Function to append"""


def append_write(filename="", text=""):
    """The function"""

    with open(filename, mode='a', encoding='utf-8') as a_file:
        nb = a_file.write(text)

    return (nb)
