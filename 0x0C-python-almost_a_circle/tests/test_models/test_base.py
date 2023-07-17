#!/usr/bin/python3
"""module test_base"""
import unittest
from models.base import Base
from models.rectangle import Rectangle



class TestBase(unittest.TestCase):
    """ class to test base class"""
    def test_init(self):
        """ tests the init method"""
        b1 = Base()
        b2 = Base()
        b3 = Base(89)
        b4 = Base(None)
        self.assertIsInstance(b1, Base)
        self.assertTrue(hasattr(b1, "id"))
        self.assertEqual(b1.id, 1)
        self.assertNotEqual(b1.id, b2.id)
        self.assertEqual(b3.id, 89)
        self.assertIsInstance(b1.id, int)
        self.assertEqual(b4.id, 3)

    def test_type_id(self):
        """ tests differnt type of id """
        self.assertEqual(Base("str").id, "str")
        self.assertEqual(Base(1.2).id, 1.2)
        self.assertEqual(Base((4, 5)).id, (4, 5))
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])
        self.assertEqual(Base({"w": 4, "h": 5}).id, {"w": 4, "h": 5})
        self.assertEqual(Base(False).id, False)
