#!/usr/bin/python3
"""Rectangle Class which inherit from Base class"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    """Test Rectangle class begins"""

    def test_pep8(self):
        """pep8 test"""

        pep = pep8.StyleGuide(quit=True)
        chk = pep.check_files(["models/rectangle.py"])
        self.assertEqual(chk.total_errors, 0, "Found code style errors (and warnings).")

    def test_doctest(self):
        """doc testing"""

        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_rectangle_all(self):
        """all rectangle testing"""

        a = Rectangle(3,3,3,3,4)
        self.assertEqual(a.area(), 9)
        self.assertEqual(a.id, 4)
