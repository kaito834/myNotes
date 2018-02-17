#!/usr/bin/env python
# coding: utf-8
# I tested by Python 3.4.3 on Windows 8.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

# This was based on https://gist.github.com/danielrasmusonsnippet/89fd62037febf465b52b
#
# Found useful python module, pyperclip: https://github.com/asweigart/pyperclip
# According to the github repository, "Python module for cross-platform clipboard functions."
def copyStrToClipboard():
#def main():
    from tkinter import Tk

    r = Tk()
    r.withdraw()
    r.clipboard_clear()

    '''
    According Python issue 23760, I cannot copy to clipboard correctly
    when r.destory() is called after r.clipboard_append() by Python 3.4.3 on Windows 8.
    The issue happened to me, so this snippet call input() after r.clipboard_append().

    http://bugs.python.org/issue23760
    http://stackoverflow.com/questions/26321333/
    '''
    str = input("Please input string that be copied to clipboard:\n> ")
    r.clipboard_append(str)
    print('[!] Copied "{0}" to clipboard.'.format(str))
    input('Please enter if you confirmed > ')

    r.destroy()

def main():
    copyStrToClipboard()

    while input("\nWould you like to retry? (Y/N) > ").upper() == 'Y':
        print('')
        copyStrToClipboard()

if __name__ == '__main__':
    main()
