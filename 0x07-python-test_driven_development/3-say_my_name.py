#!/usr/bin/python3
"""The module
"""


def say_my_name(first_name, last_name=""):
    """
    priint a full name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if first_name == "" and last_name == "":
        print("My name is ")
    else:
        print("My name is {} {}".format(first_name, last_name))
