#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_list_equals(self):
        hello = [1,2,3,4]
        list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(hello), 4)

    def test_negative(self):
        list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list), -1)
        with self.assertRaises(SyntaxError):
            max_integer(---)

#    def test_types(self):
#        list = ["a", "b"]
#        self.assertEqual(max_integer(), [")
#        with self.assertRaises(SyntaxError):
