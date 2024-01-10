#!/usr/bin/python3
"""defining square printer"""


def print_square(size):
    """prints square with #"""
    if isinstance(size, float) and size < 0 or not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
