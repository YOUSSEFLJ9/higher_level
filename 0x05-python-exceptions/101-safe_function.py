#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        function = fct(*args)
        return function
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
