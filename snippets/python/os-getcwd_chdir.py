#!/usr/bin/env python
# coding: utf-8
# Tested by Python 3.6.3 on Windows 10
# Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32

import os
import sys

def main():
    # https://docs.python.org/3/library/os.html#os.getcwd
    currentDirStr = os.getcwd()
    changedDirStr = sys.argv[1]

    print("Current working directory: {0}".format(currentDirStr))
    try:
        # https://docs.python.org/3/library/os.html#os.chdir
        os.chdir(changedDirStr)
        print("Changed working directory to {0}".format(changedDirStr))
    # https://docs.python.org/3/library/exceptions.html#FileNotFoundError
    except FileNotFoundError as e:
        print("[!] FileNotFoundError: {0}".format(e))
    except Exception as e:
        print("[!] Exception: {0} ({1})".format(e, type(e)))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        print("Usage: {0} <directory>".format(sys.argv[0]))
