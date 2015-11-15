#!/usr/bin/env python
# coding: utf-8
#
# I tested by Python 3.4.3 on Windows 10.
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

import subprocess

# This is based on https://github.com/johndekroon/serializekiller/blob/master/serializekiller.py
# https://docs.python.org/3.4/library/subprocess.html
def main():
    cmd = 'dir /B'

    # https://docs.python.org/3.4/library/subprocess.html#popen-constructor
    # https://docs.python.org/3.4/library/subprocess.html#frequently-used-arguments
    #   > Providing a sequence of arguments is generally preferred, as it allows the module to
    #   > take care of any required escaping and quoting of arguments (e.g. to permit spaces in file names).
    #   > If passing a single string, either shell must be True (see below) or else the string must
    #   > simply name the program to be executed without specifying any arguments.
    # https://docs.python.org/3.4/library/subprocess.html#security-considerations
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # https://docs.python.org/3.4/library/subprocess.html#subprocess.Popen.communicate
    # Types of variables out and err are bytes; confirmed print(type(out))
    out, err = p.communicate()
    print('** The result of \'{0}\' is as follows:'.format(cmd))
    print('===')
    print(out.decode('utf-8'))
    print('===')

    # https://docs.python.org/3/reference/expressions.html#in
    # > For the string and bytes types, x in y is true if and only if x is a substring of y.
    # > An equivalent test is y.find(x) != -1. Empty strings are always considered to
    # > be a substring of any other string, so "" in "abc" will return True.
    if b'.py' in out:
        print('')
        print("There is/are python script(.py) in this directory")

if __name__ == '__main__':
    main()

# References:
# https://docs.python.org/3.4/library/subprocess.html
# 3.4.x and earilier 3.x
# - subprocess.call()
# - subprocess.check_call()
# - subprocess.check_output()
# - subprocess.Popen
# https://docs.python.org/3/library/subprocess.html
# https://docs.python.org/3/whatsnew/3.5.html#whatsnew-subprocess
# 3.5; maybe later 3.x too
# - subprocess.run()
# - subprocess.Popen()
