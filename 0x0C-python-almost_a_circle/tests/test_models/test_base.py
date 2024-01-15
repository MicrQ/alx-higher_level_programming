#!/usr/bin/python3
"""Test Cases for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_Cases(unittest.TestCase):
    """test cases for instantiation of task 1"""

    def test_with_or_without(self):
        """testing with passing id and without passing"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(20).id, 20)
        self.assertEqual(Base().id, 2)

        """test with argumetes"""
        self.assertEqual(12, Base(12).id)
        self.assertEqual(24, Base(24).id)
        self.assertEqual(Base(30).id, 30)

        """testing without argument to initialize"""
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base().id, 4)


"""JSON string testing"""


class TestJson(unittest.TestCase):
    """represents the json string test cases"""

    def test_to_json_string(self):
        """to_json string test of task 15"""
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle(self):
        """rectangle string"""
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        """type of square"""
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square(self):
        """one dictionary"""
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)


if __name__ == "__main__":
    unittest.main()
