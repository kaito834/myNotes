#!/usr/bin/env python
# coding: utf-8
# Tested by Python 3.5.1 on Windows 10
# Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32

# https://docs.python.org/3/library/base64.html
import base64
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: {0} <base64 string>".format(sys.argv[0]))
        exit(1)

    base64str = sys.argv[1]
    base64str += '=' * (4 - len(base64str) % 4)

    # https://docs.python.org/3/library/base64.html#base64.b64decode
    # http://stackoverflow.com/questions/2941995/python-ignore-incorrect-padding-error-when-base64-decoding
    print((base64.b64decode(base64str.encode('utf-8'), '-_')).decode('utf-8'))

if __name__ == '__main__':
    main()
