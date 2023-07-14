#!/usr/bin/python3
""" module: test_rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ it tests the class Rectangle"""
    def test_idInit(self):
        """ it tests the id after the initialization"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, -1)

        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(hasattr(r1, "id"))
        self.assertNotEqual(r1.id, r2.id)
        self.assertEqual(r3.id, -1)
        self.assertIsInstance(r1.id, int)

    def test_attributes(self):
        """ it tests the other attributes after the initialization"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, -1)

        self.assertTrue(hasattr(r1, "width"))
        self.assertTrue(hasattr(r1, "height"))
        self.assertTrue(hasattr(r1, "x"))
        self.assertTrue(hasattr(r1, "y"))
