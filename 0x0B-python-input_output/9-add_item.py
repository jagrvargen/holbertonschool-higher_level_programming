#!/usr/bin/python3
"""
   This module contains a script to add all arguments to a Python list,
   and then save them to a file.
"""


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
import sys
import json


arguments = [item for item in sys.argv[1:]]
try:
    my_obj = load_from_json_file('add_item.json')
    for item in arguments:
        my_obj.append(item)
    save_to_json_file(my_obj, 'add_item.json')
except FileNotFoundError:
    with open('add_item.json', 'w', encoding="utf-8") as fp:
        json.dump(arguments, fp)
