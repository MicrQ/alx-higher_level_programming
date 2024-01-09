#!/usr/bin/python3
"""loading"""

import json
"""JSON"""


def load_from_json_file(filename):
    """loading from json file and creating object"""
    with open(filename) as f:
        return json.load(f)
