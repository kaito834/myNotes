#!/usr/bin/env python
# coding: utf-8
# Tested by Python 3.6.1 on Windows 10
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32

import sys
# https://github.com/chardet/chardet
# chardetect, command line tool, is avaliable if you install chardet by pip
# https://github.com/chardet/chardet#command-line-tool
import chardet

def main():
    # Open file by binary mode
    # https://docs.python.org/3/library/functions.html#open
    with open(sys.argv[1], 'rb') as f:
    	contents = f.read()

    encoding = chardet.detect(contents)
    print('{0}: {1} (confidence: {2})'.format(sys.argv[1], encoding['encoding'], encoding['confidence']))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        print('Usage: {0} <filepath>'.format(sys.argv[0]))
