#!/usr/bin/env python
# coding: utf-8
#
# tested by Python 3.4.3 on Windows 8.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

import re

# https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
# http://d.hatena.ne.jp/itasuke/20090815/p1 (in Japanese)
filename=r".\\re-multilines_sample.txt"

# https://docs.python.org/3/library/functions.html#open
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
with open(filename, 'r', encoding='utf-8') as f:
	file=f.read()

# https://docs.python.org/3/library/re.html#re.DOTALL
regex=re.compile(r"\*\*section \d\n---\n(.+?)---\n\n*", re.DOTALL)
matchlist=regex.findall(file)

for m in matchlist:
	print("*** MATCHED ***\n{0}******\n\n".format(m))
