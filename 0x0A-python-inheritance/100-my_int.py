#!/usr/bin/python3
"""MyInt calss"""


class MyInt(int):
    """invertes the behavior of __eq__ and __ne__"""

    def __ne__(self, other):
        """not equal"""
        return super().__eq__(other)

    def __eq__(self, value):
        """equal"""
        return super().__ne__(value)
