#!/usr/bin/python3
"""module that defines a script that adds all arguments
to a Python list, and then save them to a file"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argv = sys.argv
if __name__ == "__main__":
    filename = "add_item.json"
    try:
        a_list = load_from_json_file(filename)
    except FileNotFoundError:
        a_list = []
    for i in range(1, len(argv)):
        a_list.append(argv[i])
    save_to_json_file(a_list, filename)
