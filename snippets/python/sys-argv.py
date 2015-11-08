#!/usr/bin/env python
# coding: utf-8
#
# I tested by Python 3.4.3 on Windows 10.
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

import sys

# https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments
# https://docs.python.org/3/library/sys.html#sys.argv
if __name__ == '__main__':
    if len(sys.argv) == 1:
        # https://docs.python.org/3/library/functions.html#print
        print("** Please execute {0} with some arguments. Exit.".format(sys.argv[0]), file=sys.stderr)
    else:
        # Reference for format string syntax
        # https://docs.python.org/3/library/string.html#formatstrings
        for i, arg in enumerate(sys.argv):
                print("sys.argv[{0}]\t{1:<20} type: {2}".format(i, arg, type(sys.argv[i])))
