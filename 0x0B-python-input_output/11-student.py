#!/usr/bin/python3
"""Student Class"""


class Student:
    """Class begin"""

    def __init__(self, first_name, last_name, age):
        """init stuff"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retriving dictionary"""

        dclass = self.__dict__
        dsel = {}

        if type(attrs) is list:
            for atr in attrs:
                if type(atr) is not str:
                    return dclass

            for k in attrs:
                if hasattr(self, k):
                    dsel[k] = getattr(self, k)
            return dsel

        return self.__dict__

    def reload_from_json(self, json):
        """reload from json dict"""

        for i in json:
            if i in self.__dict__:
                self.__dict__[i] = json[i]
