#!/usr/bin/env python
# coding: utf-8
#
# Tested by Python 3.6.3 on Windows 10
# Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32

import sys
import os
from pathlib import Path

def main():
    dirStr = sys.argv[1]

    # pp.306-307, 10.1.2, 10.1.3, 入門 Python 3, https://www.oreilly.co.jp/books/9784873117386/
    # https://docs.python.org/3/library/os.path.html#os.path.exists
    if not os.path.exists(dirStr):
        print("[!] \"{0}\" isn't found.".format(dirStr))
        exit(1)

    # https://docs.python.org/3/library/os.path.html#os.path.isdir
    if not os.path.isdir(dirStr):
        print("[!] \"{0}\" isn't a directory.".format(dirStr))
        exit(1)

    # Use os.walk()
    # https://qiita.com/suin/items/cdef17e447ceeff6e79d
    # https://docs.python.org/3.6/library/os.html#os.walk
    print("Use os.walk():\n")
    for file in getAllFile_os_walk(dirStr):
        print(file)

    print('*'*10)

    # Use Path class in pathlib module
    # https://qiita.com/amowwee/items/e63b3610ea750f7dba1b
    # https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob
    print("Use pathlib.Path.glob():\n")
    dirPath = Path(dirStr)
    # >>> type(dirPath.glob("**/*"))
    # <class 'generator'>
    for file in dirPath.glob("**/*"):
        print(file)

# https://qiita.com/suin/items/cdef17e447ceeff6e79d
#
# This fucntion is a generator, because yield is used instead of return
# https://qiita.com/tomotaka_ito/items/35f3eb108f587022fa09s
# pp.125-126 4.9 ジェネレータ, 入門 Python 3, https://www.oreilly.co.jp/books/9784873117386/
# pp.260-266 7.4 ジェネレータ, Python 文法詳解, https://www.oreilly.co.jp/books/9784873116884/
def getAllFile_os_walk(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        print("Usage: {0} <Directory>".format(sys.argv[0]))
