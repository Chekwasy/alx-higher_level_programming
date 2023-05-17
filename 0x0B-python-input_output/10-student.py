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
        dsel = dict()

        if type(attrs) is list:
            for atr in attrs:
                if type(atr) is not str:
                    return dclass

            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__