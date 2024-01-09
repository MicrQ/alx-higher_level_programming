#!/usr/bin/python3
"""writing json representation to file"""

import json
"""JSON"""


def save_to_json_file(my_obj, filename):
    """writes to a file with json string"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
