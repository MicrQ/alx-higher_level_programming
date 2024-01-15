#!/usr/bin/python3
"""Test Cases for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


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


"""testing save to json file"""


class TestJsonFile(unittest.TestCase):
    """represents the tests of json file"""

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def test_save_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_from_json_string(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_1(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_2(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r1, r2)

    """tests for load from file task 19"""
    def test_load_from_file(self):
        s = Square(5, 1, 3, 3)
        s1 = Square(9, 5, 2, 3)
        Square.save_to_file([s, s1])
        output = Square.load_from_file()
        self.assertTrue(all(type(o) == Square for o in output))

    def test_load_from_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)



if __name__ == "__main__":
    unittest.main()
