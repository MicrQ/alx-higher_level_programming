#!/usr/bin/python3
"""unittest for Square class(square file)"""


from models.square import Square
from models.base import Base
import unittest
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """representes tests of Square class"""

    def test_isinstance(self):
        """testing if Square is instance of Base
          if it is, it is also instance of Rectangle as well"""
        self.assertIsInstance(Square(5), Base)

    def test_without_size_arg(self):
        """should raise exception with no args"""
        with self.assertRaises(TypeError):
            Square()

    def test_with_args(self):
        """testing with args"""
        sq = Square(7)
        self.assertEqual(Square(9).id, sq.id + 1)
        self.assertEqual(Square(20).width, 20)
        self.assertEqual(Square(20).height, 20)
        sq1 = Square(20, 10, 12, 33)
        self.assertEqual(sq1.width, 20)
        self.assertEqual(sq1.height, 20)
        self.assertEqual(sq1.x, 10)
        self.assertEqual(sq1.y, 12)
        self.assertEqual(sq1.id, 33)

    def test__size(self):
        """making sure size is not private"""
        with self.assertRaises(AttributeError):
            Square(12).__size

    def test_check__str(self):
        """testing the output of __str__"""
        self.assertEqual(str(Square(2, 5, 7, 9)), "[Square] (9) 5/7 - 2")

    def test_display_square(self):
        """testing the inherited display function"""
        cap_op = StringIO()
        sys.stdout = cap_op
        expected = "\n\n  ##\n  ##\n"

        Square(2, 2, 2).display()
        self.assertEqual(cap_op.getvalue(), expected)

        cap_op1 = StringIO()
        sys.stdout = cap_op1
        expected = "\n\n    ####\n    ####\n    ####\n    ####\n"

        Square(4, 4, 2).display()
        self.assertEqual(cap_op1.getvalue(), expected)

        sys.stdout = sys.__stdout__

    def test_size_getter_setter(self):
        """testing the setter and getter of size"""
        self.assertEqual(Square(6).size, 6)
        self.assertEqual(Square(6).width, 6)
        self.assertEqual(Square(6).height, 6)
        self.assertEqual(Square(8, 3, 5, 1).size, 8)

    def test_update_method(self):
        """testing the modified update method of Square class"""
        sq = Square(20, 12, 32, 23)
        """before update"""
        self.assertEqual(sq.id, 23)
        self.assertEqual(sq.size, 20)
        self.assertEqual(sq.x, 12)
        self.assertEqual(sq.y, 32)
        """updating with args only"""
        sq.update(10, 50, 30, 40)
        self.assertEqual(sq.id, 10)
        self.assertEqual(sq.size, 50)
        self.assertEqual(sq.x, 30)
        self.assertEqual(sq.y, 40)
        """updating with both args and kwargs"""
        sq.update(20, 30, 40, 50)
        self.assertEqual(sq.id, 20)
        self.assertEqual(sq.size, 30)
        self.assertEqual(sq.x, 40)
        self.assertEqual(sq.y, 50)
        """updating with kwargs only"""
        kwargs = {"y": 10, "size": 80, "id": 30, "x": 40}
        sq.update(**kwargs)
        self.assertEqual(sq.id, 30)
        self.assertEqual(sq.size, 80)
        self.assertEqual(sq.x, 40)
        self.assertEqual(sq.y, 10)

    def test_to_dictionary_method(self):
        """testing the dictionary representation method"""
        sq = Square(3, 2, 5, 8)
        self.assertEqual(sq.to_dictionary(),
                         {"id": 8, "size": 3, "x": 2, "y": 5})
        sq.update(7, 4, 3, 10)
        self.assertEqual(sq.to_dictionary(),
                         {"id": 7, "size": 4, "x": 3, "y": 10})
