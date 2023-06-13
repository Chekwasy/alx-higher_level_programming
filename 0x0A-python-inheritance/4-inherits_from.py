#!/usr/bin/python3
"""just method"""


def inherits_from(obj, a_class):
    """methid begins"""

    if type(obj) is not a_class:
        if issubclass(type(obj), a_class):
            return True
        else:
            return False
    else:
        return False
