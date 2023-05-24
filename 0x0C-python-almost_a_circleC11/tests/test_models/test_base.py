#!/usr/bin/python3
"""A file that test the base class of rectangle"""
import pep8
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    """The class to test begins"""

    def test_pep8_base(self):
        """The pep8 testing function for the base class"""

        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )
        
