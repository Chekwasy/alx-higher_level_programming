#!/usr/bin/python3
"""Check for subclass"""


def inherits_from(obj, a_class):
    """The function to check the subclass"""

    if isinstance(obj, a_class):
        if issubclass(a_class, obj.__class__) is False:
            return True
    else:
        return False
