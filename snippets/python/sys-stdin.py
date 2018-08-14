#!/usr/bin/env python
# coding: utf-8
# Tested by Python 3.6.1 on Windows 10
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32

import sys

def main():
    print("Output strings from stdin which is not interactive shell; redirect or pipe:")
    print("***")

    # https://docs.python.org/3/library/sys.html#sys.stdin
    # https://www.lifewithpython.com/2017/06/python-check-stdin-type.html (in Japanese)
    if not sys.stdin.isatty():
        for line in sys.stdin:
            # https://docs.python.org/3/library/stdtypes.html#str.rstrip
            print(line.rstrip("\r\n"))
    else:
        print("NO INPUT FROM REDIRECT OR PIPE")

if __name__ == '__main__':
    main()
