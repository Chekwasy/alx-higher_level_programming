#!/usr/bin/python3
"""Square class"""
import unittest
import pep8
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test for Square begins"""

    def test_pep8(self):
        """pep8 test case"""

        pep = pep8.StyleGuide(quit=True)
        chk = pep.check_files(["models/square.py"])
        self.assertEqual(chk.total_errors, 0, "Found code style errors (and warnings).")

    def test_doctest(self):
        """doc test"""

        self.assertTrue(len(Base.__doc__) >= 1)

    def test_sqauare_all_positive(self):
        """square testing"""

        a = Square(3,3,3,3)
        self.assertEqual(a.area(), 9)
        self.assertEqual(a.id, 3)
