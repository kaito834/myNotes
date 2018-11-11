#!/usr/bin/env python
# coding: utf-8

import os
import sys
# https://github.com/kaito834/myNotes/blob/master/snippets/python/magic_from_file.py
import magic
# https://github.com/kaito834/myNotes/blob/master/notes/detectSecreOnSourceCodeRepository.md#trufflehog
# https://github.com/dxa4481/truffleHog
from pathlib import Path
# https://github.com/kaito834/myNotes/blob/master/snippets/python/detect-encodeing-by-chardet.py
# https://chardet.readthedocs.io/en/latest/usage.html#advanced-usage
from chardet.universaldetector import UniversalDetector

def main():
    dirStr = sys.argv[1]

    # https://github.com/kaito834/myNotes/blob/master/snippets/python/getAllFilesInDir.py
    if not os.path.exists(dirStr):
        print("[!] \"{0}\" isn't found.".format(dirStr))
        exit(1)
    if not os.path.isdir(dirStr):
        print("[!] \"{0}\" isn't a directory.".format(dirStr))
        exit(1)

    # https://github.com/kaito834/myNotes/blob/master/snippets/python/getAllFilesInDir.py
    dirPath = Path(dirStr)
    for file in dirPath.glob("**/*"):
        # type(file): <class 'pathlib.WindowsPath'>
        # type(file.as_posix()): <class 'str'>
        if not os.path.isdir(file.as_posix()):
            listTextBasedFiles(file.as_posix())

def listTextBasedFiles(file):
    try:
        # Detect MIME type for file
        # https://github.com/kaito834/myNotes/blob/master/snippets/python/magic_from_file.py
        # https://github.com/ahupp/python-magic#usage
        f_mimetype = magic.from_file(file, mime=True)
    except Exception as e:
        print("[!] Exception: {0} ({1})".format(e, type(e)))

    # Open and count lines if MIME type of the file is text/*
    if f_mimetype.split('/')[0] == 'text':
        # Detect encoding by chardet.universaldetector.UniversalDetector()
        # https://chardet.readthedocs.io/en/latest/usage.html#advanced-usage
        detector = UniversalDetector()
        with open(file, 'rb') as f:
            for line in f.readlines():
                detector.feed(line)
                if detector.done:
                    break
        detector.close()

        with open(file, "r", encoding=detector.result['encoding']) as f:
            line_count = 0
            for line in f.readlines():
                line_count += 1
            print("{0}: {1}, {2}, {3} lines".format(file, f_mimetype, detector.result['encoding'], line_count))
    else:
        print("{0}: NOT txet based file (reason: MIME type isn't text/*: {1})".format(file, f_mimetype))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        print("Usage: {0} <Directory>".format(sys.argv[0]))
