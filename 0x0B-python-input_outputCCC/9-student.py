#!/usr/bin/python3
"""Student Class"""


class Student:
    """Class begin"""

    def __init__(self, first_name, last_name, age):
        """init stuff"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retriving dictionary"""

        return self.__dict__
