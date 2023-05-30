#!/usr/bin/python3
"""Base Class"""
import json
import os


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
            return str(emt)
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class meth. to save list of inst. meth. of rec. or sq."""

        emt = []
        filename = str(cls.__name__)+".json"
        if list_objs is None:
            with open(filename, 'w', encoding='utf-8') as file1:
                file1.write(str(emt))
        else:
            for ins in list_objs:
                dit = ins.to_dictionary()
                emt.append(dit)
            jstr = Base.to_json_string(emt)
            with open(filename, 'w', encoding="utf-8") as file1:
                file1.write(jstr)
