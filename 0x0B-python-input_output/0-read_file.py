#!/usr/bin/python3
"""defining a function to read from a file"""


def read_file(filename=""):
    """reads from file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
