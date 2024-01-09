#!/usr/bin/python3
"""from json to string"""

import json
"""JSON"""


def from_json_string(my_str):
    """from json string to object"""
    return json.loads(my_str)
