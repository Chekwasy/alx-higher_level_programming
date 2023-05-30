#!/usr/bin/python3
"""Base Class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method to turn list with dictionaries to json
        string
        """
        emt = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return emt
        else:
            return json.dumps(list_dictionaries)
