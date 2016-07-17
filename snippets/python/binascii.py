#!/usr/bin/env python
# coding: utf-8
# Tested by Python 3.4.3 on Windows 10
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

# https://docs.python.org/3/library/binascii.html
import binascii

a_str = 'Hello, world!'
u_str = 'こんにちは！'

# Convert unicode string to hex representation
# Ref.
# http://qiita.com/atsaki/items/6120cad2e3c448d774bf (in Japanese)
# https://docs.python.org/3/library/binascii.html#binascii.hexlify
print('Convert unicode string to hex representation:')
# type(binascii.hexlify()): <class 'bytes'>
a_str_hex = binascii.hexlify(a_str.encode('utf-8'))
u_str_hex = binascii.hexlify(u_str.encode('utf-8'))
print("{0}\n=> {1}".format(a_str, a_str_hex))
print("{0}\n=> {1}".format(u_str, u_str_hex))

# Convert hex string to Unicode string
# Ref.
# http://qiita.com/atsaki/items/6120cad2e3c448d774bf (in Japanese)
# https://docs.python.org/3/library/binascii.html#binascii.unhexlify
print("\nConvert hex string to Unicode string:")
# type(binascii.unhexlify()): <class 'bytes'>
a_str_hex_unicode = binascii.unhexlify(a_str_hex).decode('utf-8')
u_str_hex_unicode = binascii.unhexlify(u_str_hex).decode('utf-8')
print("{0}\n=> {1}".format(a_str_hex, a_str_hex_unicode))
print("{0}\n=> {1}".format(u_str_hex, u_str_hex_unicode))

# Read a file, and convert the file content to hex representation
# Ref. https://docs.python.org/3/library/functions.html#open
filename = './resources/sample.xml'
print("\nRead {0}, and convert the file content to hex representation:".format(filename))
with open(filename, mode='br') as f:
    # type(contents): <class 'bytes'>
    contents = f.read()
print("=>\n{0}".format(binascii.hexlify(contents)))
