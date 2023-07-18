#!/usr/bin/python3
"""module test_square"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """ tests class Square"""
    def test_init(self):
        """ tests intialisation of Square object"""
        with self.assertRaises(TypeError):
            Square()

        s1 = Square(2)
        s2 = Square(5)
        self.assertNotEqual(s1.id, s2.id)

    def test_2_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertNotEqual(s1.id, s2.id)

    def test_3_args(self):
        s1 = Square(5, 2, 1)
        s2 = Square(2, 2, 1)
        self.assertNotEqual(s1.id, s2.id)

    def test_4_args(self):
        self.assertEqual(12, Square(10, 2, 2, 12).id)

    def test_more_than_4_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_attributes(self):
        """ it tests the other attributes after the initialization"""
        s1 = Square(10, 2)

        self.assertTrue(hasattr(s1, "id"))
        self.assertTrue(hasattr(s1, "size"))
        self.assertTrue(hasattr(s1, "x"))
        self.assertTrue(hasattr(s1, "y"))

    def test_size(self):
        r = Square(5)
        self.assertEqual(5, r.size)
        r.size = 10
        self.assertEqual(10, r.size)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(2.5)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("a")

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2])

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2))

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1})

        with self.assertRaises(AttributeError):
            print(Square(5).__size)

    def test_height(self):
        r = Square(5)
        self.assertEqual(5, r.height)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x(self):
        r = Square(5, 2, 4, 8)
        self.assertEqual(2, r.x)
        r.x = 10
        self.assertEqual(10, r.x)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -8, 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None, 0, 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 1.5, 2, 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "a", 2)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, [1, 2], 5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, True, 5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, (1, 2), 2)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, {"a": 1}, 2)

        with self.assertRaises(AttributeError):
            print(Square(5, 1, 0, 1).__x)

    def test_y(self):
        r = Square(2, 4, 8, 1)
        self.assertEqual(8, r.y)
        r.y = 10
        self.assertEqual(10, r.y)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 1, -8, 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, None, 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, 1.5, 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, "a", 2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, [1, 2], 5)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, True, 5)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, (1, 2), 2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 3, {"a": 1}, 2)

        with self.assertRaises(AttributeError):
            print(Square(5, 1, 0, 1).__y)

    def test_priorities(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("wrong_size", "wrong_x")

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("wrong_size", 1, "wrong_y")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "wrong_x", "wrong_y")

    def test_area(self):
        s = Square(2)
        with self.assertRaises(TypeError):
            s.area(1)
        self.assertEqual(4, s.area())
        s.size = 5
        self.assertEqual(25, s.area())

    def test_to_dictionary(self):
        """ tests method to dictionary"""
        s = Square(10, 1, 1, 1)
        result = {'size': 10, 'x': 1, 'y': 1, 'id': 1}
        self.assertDictEqual(result, s.to_dictionary())

        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)

    def test_update(self):
        """ tests update method"""
        r1 = Square(10, 10, 10)
        r1.update()
        self.assertEqual(f"[Square] ({r1.id}) 10/10 - 10", str(r1))

        r1.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(r1))

        r1.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(r1))

    def test_update_more_args(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 1, 4, 5, 6)
        self.assertEqual("[Square] (89) 4/5 - 1", str(r))

    def test_update__None_id(self):
        r = Square(10, 10, 10, 10)
        r.update(None)
        self.assertEqual(f"[Square] ({r.id}) 10/10 - 10", str(r))

        r.update(id=None)
        self.assertEqual(f"[Square] ({r.id}) 10/10 - 10", str(r))

    def test_priorities(self):
        r = Square(10, 10, 10, 10)
        r.update(1, 2, x=1, y=2)
        self.assertEqual("[Square] (1) 10/10 - 2", str(r))
