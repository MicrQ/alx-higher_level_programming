#!/usr/bin/python3
"""writeing to file"""


def write_file(filename="", text=""):
    """writes to a filename the text"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
