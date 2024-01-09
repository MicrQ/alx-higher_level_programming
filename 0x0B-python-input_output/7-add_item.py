#!/usr/bin/python3
"""argv to list"""

from sys import argv
"""importing argv"""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""importing function"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""importing function"""
try:
    the_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    the_list = []

for i in range(1, len(argv)):
    the_list.append(argv[i])
save_to_json_file(the_list, "add_item.json")
