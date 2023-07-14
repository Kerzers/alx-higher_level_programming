#!/usr/bin/python3
"""module test_base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ class to test base class"""
    def test_init(self):
        """ tests the init method"""
        b1 = Base()
        b2 = Base()
        b3 = Base(89)
        self.assertIsInstance(b1, Base)
        self.assertTrue(hasattr(b1, "id"))
        self.assertEqual(b1.id, 1)
        self.assertNotEqual(b1.id, b2.id)
        self.assertEqual(b3.id, 89)
        self.assertIsInstance(b1.id, int)
