#!/usr/bin/python3
"""Test Cases for Base class"""
import unittest
from models.base import Base


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





if __name__ == "__main__":
    unittest.main()