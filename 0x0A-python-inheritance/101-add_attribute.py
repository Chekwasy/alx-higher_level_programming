#!/usr/bin/python3
"""creat attribute of a class"""


def add_attribute(mc, name, jo):
    """funtion to add attribute"""

    if not hasattr(mc, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(mc, name, jo)
