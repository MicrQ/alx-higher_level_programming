#!/usr/bin/python3
"""Defining matrix divider function"""


def matrix_divided(matrix, div):
    """Divides each element of each row by div

    Args:
        matrix (list of lists):
        div (int or float):
    Return:
        list of list
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    row_len = None
    if (type(matrix) is not list or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(elem, int) or isinstance(elem, float))
                for elem in [num for row in matrix for num in row])):
        raise TypeError(msg)

    for row in matrix:
        if row_len is None:
            row_len = len(row)
        elif row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(col/div, 2) for col in row] for row in matrix]
