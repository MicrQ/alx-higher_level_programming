#!/usr/bin/python3
"""pascal_triangle"""


def factorial(x):
    """factorial calculator"""
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


def coeff(n, k):
    """binomial coefficient"""
    return factorial(n) // (factorial(k) * factorial(n - k))


def pascal_triangle(n):
    """defining pascal_triangle"""
    the_list = []
    for row in range(n):
        tmp = []
        for col in range(row + 1):
            tmp.append(coeff(row, col))
        the_list.append(tmp)
    return the_list
