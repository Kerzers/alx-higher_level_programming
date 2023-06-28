#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """function that prints an integer safetly"""

    try:
        print("{:d}".format(value))
        return True

    except (ValueError, TypeError) as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)
        return False
