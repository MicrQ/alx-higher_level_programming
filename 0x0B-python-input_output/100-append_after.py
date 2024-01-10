#!/usr/bin/python3
"""appending after a line that contains a given word"""


def append_after(filename="", search_string="", new_string=""):
    """appends after searching"""
    to_write = ''
    with open(filename, "r") as f:
        line = f.readline()
        while(line != ''):
            to_write += line
            if search_string in line:
                to_write += new_string
            line = f.readline()
    with open(filename, "w") as f:
        f.write(to_write)
