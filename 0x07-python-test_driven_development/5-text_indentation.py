#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""module"""


def text_indentation(text):
    """
    prints a string with 2 new lines after '.', '?', and ':'
     """

    if type(text) is not str:
        raise TypeError("text must be a string")

    string = text.replace('.', '.\n\n').replace(':', ':\n\n')\
                                       .replace('?', '?\n\n')
    for i in range(len(text)):
        string = string.replace('\n ', '\n')

    print(string, end='')
