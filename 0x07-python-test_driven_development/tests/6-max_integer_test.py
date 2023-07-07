#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class to test write unittests for the function:
    def max_integer(list=[])"""

    def test_maxList(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([-10, -5, -1, -2]), -1)
        self.assertEqual(max_integer([4025687, 1000000, 5000000]), 5000000)
        self.assertEqual(max_integer([-2, 0, 45]), 45)
