#!/usr/bin/env python
# coding: utf-8
# Tested by Python 3.6.1 on Windows 10
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32

import glob

def main():
    # https://docs.python.org/3/library/glob.html
    print("** Match .py files on working directory")
    for file in glob.glob('*.py'):
        print(file)
    print()

    print("** Match only any files on some directories from working directory")
    for file in glob.glob('**/*'):
        print(file)
    print()

    # https://docs.python.org/3/library/glob.html#glob.glob
    # If recursive is true, the pattern “**” will match any files and zero or more directories and subdirectories.
    print("** Match any files recursively from working directory")
    for file in glob.glob('**/*', recursive=True):
        print(file)
    print()

if __name__ == '__main__':
    main()
