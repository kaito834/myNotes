#!/usr/bin/env python
# coding: utf-8
#
# Python wrapper for dpapibridge, developed by @vincepare on GitHub
# https://github.com/vincepare/DPAPIbridge
#
# Reference for Windows Data Protection API (DPAPI)
# - https://digital-forensics.sans.org/summit-archives/dfirprague14/Give_Me_the_Password_and_Ill_Rule_the_World_Francesco_Picasso.pdf
#   * Find this document by googling "DPAPI SANS"
#
# Tested by Python 3.6.1 on Windows 10
# Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32

# https://docs.python.org/3/library/subprocess.html
import subprocess

# https://github.com/vincepare/DPAPIbridge/releases/download/1.0.0/dpapibridge.exe
DPAPIBRIDEGE_PATH = "C:\\Users\\kaito\\Downloads\\dpapibridge.exe"

# p.196 6.1.5 関数アノテーション, "Python文法詳解", https://www.oreilly.co.jp/books/9784873116884/
def encrypt(plainByte:bytes) -> str:
    '''
    Encrypt plaintext(bytes) by "dpapibridge --encrypt"
    "dpapibridge --encrypt" encrypt plaintext by user-specific encryption key
    '''
    dpapibridge_args = [
        DPAPIBRIDEGE_PATH,
        '--encrypt'
    ]

    # https://docs.python.org/3/library/subprocess.html#subprocess.run
    try:
        dpapibrige_result = subprocess.run(dpapibridge_args, input=plainByte, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        # https://docs.python.org/3/library/stdtypes.html#str.rstrip
        # string.whitespace include '\r' and '\n'
        # Refer to https://docs.python.org/3.6/library/string.html#string.whitespace
        return dpapibrige_result.stdout.decode('utf-8').rstrip()
        # return dpapibrige_result
    except FileNotFoundError as e:
        print('FileNotFoundError: {0}'.format(e))
        return ''
    # https://docs.python.org/3/library/subprocess.html#subprocess.CalledProcessError
    except subprocess.CalledProcessError as e:
        print('CalledProcessError: {0}'.format(e))
        return ''

# p.196 6.1.5 関数アノテーション, "Python文法詳解", https://www.oreilly.co.jp/books/9784873116884/
def decrypt(encryptedText:str) -> bytes:
    '''
    Decrypt ecrypted text by "dpapibridge --decrypt"
    "dpapibridge --decrypt" decrypt encrypted text by user-specific encryption key
    '''
    dpapibridge_args = [
        DPAPIBRIDEGE_PATH,
        '--decrypt',
        encryptedText
    ]

    try:
        dpapibrige_result = subprocess.run(dpapibridge_args, input=encryptedText.encode('utf-8'), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return dpapibrige_result.stdout.decode('utf-8').rstrip().encode('utf-8')
        # return dpapibrige_result
    except FileNotFoundError as e:
        print('FileNotFoundError: {0}'.format(e))
        return ''
    except subprocess.CalledProcessError as e:
        print('CalledProcessError: {0}'.format(e))
        return ''
