#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
import os
from io import StringIO
import pep8

class TestBase(unittest.TestCase):
    """Tests for class Base"""
    def test_id(self):
        base = Base()
        self.asssertEqual(base.id, 1)

if __name__ == "__main__":
    unittest.main()
