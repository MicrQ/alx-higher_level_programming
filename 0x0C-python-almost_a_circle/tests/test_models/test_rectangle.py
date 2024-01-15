#!/usr/bin/python3
"""Test for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangleInit(unittest.TestCase):
    """tests for rectangle instantiation of task 2"""

    def test_isinstance(self):
        """testing if Rectangle class inherits from Base"""
        self.assertTrue(isinstance(Rectangle(3, 4), Base))
        self.assertIsInstance(Rectangle(3, 4), Base)

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


""""tesing the display method"""


class TestDisplay(unittest.TestCase):
    """tests the output of the display function"""

    def test_printed(self):
        """testing the output of the method"""
        """creating object to capture from stdout"""
        cap_op = StringIO()
        """redirecting the stdout to StringIO object"""
        sys.stdout = cap_op

        Rectangle(2, 3).display()
        self.assertEqual(cap_op.getvalue(), "##\n##\n##\n")

        """restoring the stdout"""
        sys.stdout = sys.__stdout__

    def test_printed1(self):
        """testing the output of the method"""
        """creating object to capture from stdout"""
        cap_op1 = StringIO()
        """redirecting the stdout to StringIO object"""
        sys.stdout = cap_op1

        Rectangle(4, 4).display()
        self.assertEqual(cap_op1.getvalue(), "####\n####\n####\n####\n")

        """restoring the stdout"""
        sys.stdout = sys.__stdout__

    def test_printed2(self):
        """testing the output of the method"""
        """creating object to capture from stdout"""
        cap_op2 = StringIO()
        """redirecting the stdout to StringIO object"""
        sys.stdout = cap_op2

        Rectangle(6, 4).display()
        op = "######\n######\n######\n######\n"
        self.assertEqual(cap_op2.getvalue(), op)

        """restoring the stdout"""
        sys.stdout = sys.__stdout__

    def test_no_arg_4display(self):
        """no argument needed"""
        with self.assertRaises(TypeError):
            Rectangle(3, 4).display(5)

    """Display test with x and y"""
    def test_display_x_y(self):
        """handling x and y as well"""
        expected = "\n\n  ##\n  ##\n"
        cap_op = StringIO()
        sys.stdout = cap_op

        Rectangle(2, 2, 2, 2).display()
        self.assertEqual(cap_op.getvalue(), expected)
        sys.stdout = sys.__stdout__

    def test_display_x_y_2(self):
        """handling x and y as well"""
        expected = "\n\n\n  ###\n  ###\n  ###\n  ###\n"
        cap_op = StringIO()
        sys.stdout = cap_op

        Rectangle(3, 4, 2, 3).display()
        self.assertEqual(cap_op.getvalue(), expected)
        sys.stdout = sys.__stdout__

    def test_no_arg_4display2(self):
        """no argument needed"""
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 2, 5).display(5)


"""test for __str__ overriding"""


class Test__str__(unittest.TestCase):
    """testing the overriden method __str__"""

    def test_correct_return(self):
        test1 = "[Rectangle] (12) 2/3 - 8/9"
        self.assertEqual(str(Rectangle(8, 9, 2, 3, 12)), test1)

        test1 = "[Rectangle] (7) 2/4 - 8/9"
        self.assertEqual(str(Rectangle(8, 9, 2, 4, 7)), test1)

        test1 = "[Rectangle] (12) 0/0 - 8/9"
        self.assertEqual(str(Rectangle(8, 9, 0, 0, 12)), test1)


"""tests for update method"""


class TestUpdateMethod(unittest.TestCase):
    """testing the update method"""

    def test_correct_update(self):
        """with valid args"""
        beforeUpdate = "[Rectangle] (16) 12/23 - 6/9"
        afterUpdate = "[Rectangle] (89) 3/4 - 7/8"
        rect = Rectangle(6, 9, 12, 23, 16)
        self.assertEqual(str(rect), beforeUpdate)
        rect.update()
        self.assertEqual(str(rect), beforeUpdate)
        rect.update(89, 7, 8, 3, 4)
        self.assertEqual(str(rect), afterUpdate)

    def test_update_invalid_args(self):
        """with invalid args"""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid", 6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 4, 7, 4)

    """tests for update method with args and kwargs"""
    def test_update_with_args_kwargs(self):
        """kwargs will take place if len(args) == 0(if args is empty)"""
        r = Rectangle(10, 10, 10, 10, 10)
        args = (4, 7, 3, 8, 2)
        kwargs = {"id": 40, "width": 70, "height": 30, "x": 80, "y": 20}
        r.update(*args, **kwargs)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 2)

    def test_update_with_kwargs_only(self):
        """without or empty *args"""
        r = Rectangle(10, 10, 10, 10, 10)
        kwargs = {"id": 40, "width": 70, "height": 30, "x": 80, "y": 20}
        r.update(**kwargs)
        self.assertEqual(r.id, 40)
        self.assertEqual(r.width, 70)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 80)
        self.assertEqual(r.y, 20)

    def test_update_with_args_only(self):
        """without or empty *kwargs"""
        r = Rectangle(10, 10, 10, 10, 10)
        args = (40, 70, 30, 80, 20)
        r.update(*args)
        self.assertEqual(r.id, 40)
        self.assertEqual(r.width, 70)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 80)
        self.assertEqual(r.y, 20)

    def test_to_dictionary_method(self):
        """testing the dictionary representation of rectangle"""
        self.assertEqual(Rectangle(2, 3, 4, 5, 6).to_dictionary(),
                         {"id": 6, "width": 2, "height": 3, "x": 4, "y": 5})
        self.assertEqual(Rectangle(4, 7, 2, 9, 5).to_dictionary(),
                         {"id": 5, "width": 4, "height": 7, "x": 2, "y": 9})


if __name__ == "__main__":
    unittest.main()
