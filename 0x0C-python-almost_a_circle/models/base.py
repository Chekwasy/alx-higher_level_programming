#!/usr/bin/python3
"""Base Class"""


class Base:
    """Base class Begins"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization stuff"""

        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
