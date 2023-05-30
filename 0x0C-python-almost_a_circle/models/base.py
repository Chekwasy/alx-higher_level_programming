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

    @staticmethod
    def from_json_string(json_string):
        """static method to change json string rep. to pyth. understd. str"""

        emt = []
        if json_string is None or len(json_string) == 0:
            return emt
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creating instance from a dictionary"""

        if str(cls.__name__) is "Rectangle":
            dummy = cls(2, 3)
        if str(cls.__name__) is "Square":
            dummy = cls(3)
        if len(dictionary) > 0:
            dummy.update(**dictionary)
        return dummy
