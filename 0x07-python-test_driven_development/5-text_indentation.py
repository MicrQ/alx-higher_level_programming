#!/usr/bin/python3
"""text_indentation"""


def text_indentation(text):
    """2 * \n after ., ?, :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for dlm in ".:?":
        text = (dlm + "\n\n").join(
            [line.strip(" ") for line in text.split(dlm)])

    print(text, end="")
