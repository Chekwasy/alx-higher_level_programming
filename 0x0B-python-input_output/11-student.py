#!/usr/bin/python3
"""student class"""


class Student:
    """class begins"""

    def __init__(self, first_name, last_name, age):
        """init method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """class to dict method"""

        dct = {}
        if attrs is not None:
            if type(attrs) is list:
                for a in attrs:
                    if type(a) is str:
                        if hasattr(self, a):
                            dct[a] = getattr(self, a)
                if len(dct) != 0:
                    return dct
        return self.__dict__

    def reload_from_json(self, json):
        """reload from json method"""

        for a, b in json.items():
            setattr(self, a, b)
