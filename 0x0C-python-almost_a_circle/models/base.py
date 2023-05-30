#!/usr/bin/python3
"""Base Class"""
import json
import os
import csv
import turtle


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

        if str(cls.__name__) == "Rectangle":
            dummy = cls(2, 3)
        if str(cls.__name__) == "Square":
            dummy = cls(3)
        if len(dictionary) > 0:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """class method that returns list of instances from a file"""

        emt = []
        filename = ""
        if str(cls.__name__) == "Rectangle":
            filename = "Rectangle.json"
        if str(cls.__name__) == "Square":
            filename = "Square.json"
        if not os.path.exists(filename):
            return emt
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file1:
                txt = file1.read()
                jsn = Base.from_json_string(txt)
                for i in jsn:
                    inst = cls.create(**i)
                    emt.append(inst)
        return emt

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class meth. to save list of inst. meth. of rec. or sq. in csv"""

        emt = []
        filename = str(cls.__name__)+".csv"
        if list_objs is None:
            with open(filename, 'w', encoding='utf-8') as file1:
                csv.writer(str(emt))
        else:
            if os.path.exists(filename):
                os.remove(filename)
            for ins in list_objs:
                dit = ins.to_dictionary()
                for i, j in dit.items():
                    emt.append(j)
                with open(filename, 'a', encoding="utf-8") as file1:
                    csvobj = csv.writer(file1)
                    csvobj.writerow(emt)
                    emt = []

    @classmethod
    def load_from_file_csv(cls):
        """class method that returns list of instances from a file via csv"""

        emt = []
        filename = ""
        if str(cls.__name__) == "Rectangle":
            filename = "Rectangle.csv"
        if str(cls.__name__) == "Square":
            filename = "Square.csv"
        if not os.path.exists(filename):
            return emt
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file1:
                csv_txt = csv.reader(file1)
                for i in csv_txt:
                    if str(cls.__name__) == "Rectangle":
                        ditt = {"id": int(i[0]), "width": int(i[1]),
                                "height": int(i[2]),
                                "x": int(i[3]), "y": int(i[4])}
                    if str(cls.__name__) == "Square":
                        ditt = {"id": int(i[0]), "size": int(i[1]),
                                "x": int(i[2]), "y": int(i[3])}
                    inst = cls.create(**ditt)
                    emt.append(inst)
        return emt

    @staticmethod
    def draw(list_rectangles, list_squares):
        """static method to draw squares and rectangles"""

        tur = turtle.Turtle()
        Turtle.screen()
        tur.forward(list_rectangles[0].width)
        tur.left(list_rectangles[0].height)
        tur.backward(list_rectangles[0].width)
        tur.right(list_rectangles[0].height)
