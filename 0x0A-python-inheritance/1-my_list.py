#!/usr/bin/python3
"""Defines a list class"""


class MyList(list):
    """Inherites from list class"""

    def print_sorted(self):
        """prints the list by asc order"""
        print(sorted(self))
