#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """ function that executes a function safely.
    Args:
    fct: pointer to a function
    args: arguments of fct

    Returns:
    the result of the function, Otherwise, returns None
    """
    try:
        return fct(*args)

    except Exception as err:
        print("Exception: {}".format(str(err)), file=sys.stderr)
        return None
