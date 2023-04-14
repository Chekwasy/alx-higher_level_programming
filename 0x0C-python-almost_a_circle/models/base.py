#!/usr/bin/python3
"""base class"""


class Base:
    """The class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init stuff"""

        if id == None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
            self.id = id
        else:
            self.id = id
