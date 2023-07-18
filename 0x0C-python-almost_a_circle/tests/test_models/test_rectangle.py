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
        r = Rectangle(1, 2, 3, 4, None)
        _r = Rectangle(1, 2, 3, 4)
        self.assertNotEqual(r.id, _r.id)

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

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(5, 0, 1)

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

    def test_area(self):
        """ tests area of rectangle"""
        r = Rectangle(2, 4)
        with self.assertRaises(TypeError):
            r.area(1)
        self.assertEqual(8, r.area())
        r.width = 5
        self.assertEqual(20, r.area())

    def test_to_dictionary(self):
        """tests tp_dictionary method of a rectangle"""
        r = Rectangle(10, 2, 1, 9, 5)
        result = {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertDictEqual(result, r.to_dictionary())

        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

        r = Rectangle(1, 2, 4, 1, 1)
        with self.assertRaises(TypeError):
            r.to_dictionary(2)

    def test_update(self):
        """ tests update method"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        self.assertEqual(f"[Rectangle] ({r1.id}) 10/10 - 10/10", str(r1))

        r1.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r1))

        r1.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r1))

    def test_update_more_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 1/2", str(r))

    def test_update__None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        self.assertEqual(f"[Rectangle] ({r.id}) 10/10 - 10/10", str(r))

        r.update(id=None)
        self.assertEqual(f"[Rectangle] ({r.id}) 10/10 - 10/10", str(r))

    def test_priorities(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(1, 2, x=1, y=2)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))
