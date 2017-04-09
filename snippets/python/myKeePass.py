#!/usr/bin/env python
# coding: utf-8
# Tested by Python 3.6.1 on Windows 10
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32

import getpass
import subprocess

# Ref. p.216- 6.4 クラス, "Python文法詳解", https://www.oreilly.co.jp/books/9784873116884/
class myKeePass:
    def __init__(self):
        self.__keepass_path = "C:\\Users\\kaito\\Documents\\mydata\\KeePass\\KeyPass.exe"
        self.__kpscript_path = "C:\\Users\\kaito\\Documents\\mydata\\KeePass\\KPScript.exe"
        self.__kdbx_path = "C:\\Users\\kaito\\Documents\\mydata\\kdbx\\myDatabase.kdbx"
        self.__masterKey = ""

    def setMasterKey(self):
        '''Set Master Key to open KDBX file via stdin
        Will fail to execute KPScript command if this master key is incorrect
        '''
        # https://docs.python.org/3/library/getpass.html
        self.__masterKey = getpass.getpass('Please input MasterKey: ')

    # p.196 6.1.5 関数アノテーション, "Python文法詳解", https://www.oreilly.co.jp/books/9784873116884/
    def getPasswdFromKdbx(self, refTitle:str) -> str:
        '''Get the password via KPScript 'GeEntryString' command
        The password is stored on *refTitle* entry on KDBX file

        Reference:
        - http://keepass.info/help/v2_dev/scr_sc_index.html#getentrystring
        '''
        kpscript_args = [
            self.__kpscript_path,
            '-c:GetEntryString',
            self.__kdbx_path,
            "-pw:{0}".format(self.__masterKey),
            '-Field:Password',
            "-ref-Title:{0}".format(refTitle)
        ]

        try:
            # https://docs.python.org/3.4/library/subprocess.html#subprocess.check_output
            # ... If used it must be a byte sequence, or a string if universal_newlines=True. ...
            kpscript_result = subprocess.check_output(kpscript_args, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            # https://docs.python.org/3.4/library/subprocess.html#subprocess.CalledProcessError
            print(type(e))
            # NOTE: Valid or invalid master key will be outputted if print(e.cmd) is commented out
            # print(e.cmd)
            print(e.output)

        # https://docs.python.org/3/library/stdtypes.html#str.splitlines
        return kpscript_result.splitlines()[0]
