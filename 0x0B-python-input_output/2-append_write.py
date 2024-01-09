#!/usr/bin/python3
"""appendding to file || creating the file if doesn't exist"""


def append_write(filename="", text=""):
    """appends to text"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
