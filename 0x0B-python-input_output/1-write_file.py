#!/usr/bin/python3
"""Writing function"""


def write_file(filename="", text=""):
    """The Function"""

    with open(filename, mode='w', encoding='utf-8') as a_file:
        nb = a_file.write(text)
    return (nb)
