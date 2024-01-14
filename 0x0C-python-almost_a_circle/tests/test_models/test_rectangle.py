#!/usr/bin/python3
"""Test for Rectangle class"""
import unittest
from models.rectangle import Rectangle

class TestRectangleInit(unittest.TestCase):
    """tests for rectangle instantiation of task 2"""

    def test_no_parameters(self):
        """exception for no argument for width and height"""
        with self.assertRaises(TypeError):
            """with no arg"""
            Rectangle()
        with self.assertRaises(TypeError):
            """one arg"""
            Rectangle(23)

    def test_width(self):
        """testing the width only"""
        recw = Rectangle(5, 4, 3, 2, 7)
        self.assertEqual(recw.width, 5)

    def test_height(self):
        """testing the height only"""
        rech = Rectangle(5, 4, 3, 2, 7)
        self.assertEqual(rech.height, 4)

    def test_x(self):
        """testing the x only"""
        recx = Rectangle(5, 4, 3, 2, 7)
        self.assertEqual(recx.x, 3)

    def test_y(self):
        """testing the y only"""
        recy = Rectangle(5, 4, 3, 2, 7)
        self.assertEqual(recy.y, 2)

    def test_with_args(self):
        """testing all argumentes together"""
        rec1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rec1.width, 1)
        self.assertEqual(rec1.height, 2)
        self.assertEqual(rec1.x, 3)
        self.assertEqual(rec1.y, 4)
        self.assertEqual(rec1.id, 5)

    def test_more_args(self):
        """testing with more that 5 args"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

"""task 3"""
class TestRectangleValidation(unittest.TestCase):
    """tests for rectangle validation with setters and getters"""

    def test_typeExceptions(self):
        """all args except id should be integer"""
        with self.assertRaises(TypeError):
            Rectangle("width", "height", "x", "y")
        with self.assertRaises(TypeError):
            Rectangle("width", 3, 5, 6)
        with self.assertRaises(TypeError):
            Rectangle(5, "height", 6, 7)
        with self.assertRaises(TypeError):
            Rectangle(5, 6, "x", 7)
        with self.assertRaises(TypeError):
            Rectangle(5, 6, 7, "y")
        """only with two args"""
        with self.assertRaises(TypeError):
            Rectangle("width", "height")
        with self.assertRaises(TypeError):
            Rectangle(5, 3.4)
        with self.assertRaises(TypeError):
            Rectangle(3.4, 5)

    def test_valueExceptions(self):
        """width and height must be > 0"""
        with self.assertRaises(ValueError):
            Rectangle(0, 0)
        with self.assertRaises(ValueError):
            Rectangle(0, 10)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, -10)
        with self.assertRaises(ValueError):
            Rectangle(-10, 10)
        """x and y must be >= 0"""
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 0, -1)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -1, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -2, -4)

    def test_rightInputs(self):
        """testing with right inputs"""
        self.assertEqual(Rectangle(10, 5, 4, 6).y, 6)
        self.assertEqual(Rectangle(10, 5, 4, 6).x, 4)
        self.assertEqual(Rectangle(10, 5, 4, 6).height, 5)
        self.assertEqual(Rectangle(10, 5, 4, 6).width, 10)

""""testing the area method"""
class TestArea(unittest.TestCase):
    """tests the area of the rectangle objects"""

    def test_area(self):
        """testing area"""
        self.assertEqual(Rectangle(2, 3).area(), 6)
        self.assertEqual(Rectangle(7, 7).area(), 49)
        self.assertEqual(Rectangle(5, 1).area(), 5)
        """no arg needed"""
        with self.assertRaises(TypeError):
            Rectangle(3, 2).area(5)




if __name__ == "__main__":
    unittest.main()