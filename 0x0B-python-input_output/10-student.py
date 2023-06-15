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
                if len(attrs) == 0:
                    return self.__dict__
                for a in attrs:
                    if type(a) is str:
                        if hasattr(self, a):
                            dct[a] = getattr(self, a)
                if len(dct) != 0:
                    return dct
        return self.__dict__
