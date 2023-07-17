#!/usr/bin/python3
""" module: test_rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ it tests the class Rectangle"""
    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

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

    def test_arguments(self):
        """ tests arguments if the Rectangle class"""
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(0)

    def test_3_args(self):
        r1 = Rectangle(1, 3, 5)
        r2 = Rectangle(2, 6, 4)
        self.assertEqual(r1.id + 1, r2.id)

    def test_4_args(self):
        r1 = Rectangle(1, 3, 5, 2)
        r2 = Rectangle(2, 6, 4, 1)
        self.assertEqual(r1.id + 1, r2.id)

    def test_5_args(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, None).id, 8)

    def test_more_5_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width(self):
        r = Rectangle(5, 2, 4, 8, 1)
        self.assertEqual(5, r.width)
        r.width = 10
        self.assertEqual(10, r.width)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, -2, 1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2, 0, 0, 1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(2.5, 2, 1)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("a", 2)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2], 5)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 5)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 2)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1}, 2)

        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 1, 0, 1).__width)

    def test_height(self):
        r = Rectangle(5, 2, 4, 8, 1)
        self.assertEqual(2, r.height)
        r.height = 10
        self.assertEqual(10, r.height)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, -2, 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None, 2, 0, 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 2.5, 2, 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "a", 2)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2], 5)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, True, 5)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2), 2)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1}, 2)

        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 1, 0, 1).__height)

    def test_x(self):
        r = Rectangle(5, 2, 4, 8, 1)
        self.assertEqual(4, r.x)
        r.x = 10
        self.assertEqual(10, r.x)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 2, -8, 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None, 0, 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 1.5, 2, 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "a", 2)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2], 5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2), 2)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1}, 2)

        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 1, 0, 1).__x)

    def test_y(self):
        r = Rectangle(5, 2, 4, 8, 1)
        self.assertEqual(8, r.y)
        r.y = 10
        self.assertEqual(10, r.y)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(5, 2, 1, -8, 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None, 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 1.5, 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "a", 2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, [1, 2], 5)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, True, 5)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, (1, 2), 2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {"a": 1}, 2)

        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 1, 0, 1).__y)
