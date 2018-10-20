#!/usr/bin/env python
# coding: utf-8
#
# Tested by Python 3.6.3 on Windows 10
# Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32

# https://github.com/ahupp/python-magic
# https://pypi.org/project/python-magic-bin/
#
# Setup
# $> pip install python-magic
# $> pip install python-magic-bin
import magic
import sys

def main():
    try:
        # https://github.com/ahupp/python-magic#usage
        print("{0} is \"{1}\"".format(sys.argv[1], magic.from_file(sys.argv[1])))
        print("MIME type: {0}".format(magic.from_file(sys.argv[1], mime=True)))
    except FileNotFoundError as e:
        print("[!] FileNotFoundError: {0}".format(e))
    except PermissionError as e:
        print("[!] PermissionError: {0}".format(e))
        print("[!] {0} may be a directory".format(sys.argv[1]))
    except Exception as e:
        print("[!] Exception: {0} ({1})".format(e, type(e)))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        print("Usage: {0} <file>".format(sys.argv[0]))
