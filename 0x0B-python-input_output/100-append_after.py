#!/usr/bin/python3
"""appending after a line that contains a given word"""


def append_after(filename="", search_string="", new_string=""):
    """appends after searching"""
    to_write = ""
    with open(filename, "r") as fr:
        text = fr.readlines()

    with open(filename, "w") as fw:
        for line in text:
            to_write += line
            if search_string in line:
                to_write += new_string
        fw.write(to_write)
