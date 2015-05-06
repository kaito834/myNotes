#!/usr/bin/env python
#
# tested by Python 3.4.3 on Windows 8.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

import re

# https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
# http://d.hatena.ne.jp/itasuke/20090815/p1 (in Japanese)
filename=r"C:\\Users\\kaito\\Documents\\mydata\\scripts\\re-multilines_sample.txt"

# https://docs.python.org/3/library/functions.html#open
# https://docs.python.org/3/tutorial/inputoutput.html
file=open(filename, 'r', encoding='utf-8').read()

# https://docs.python.org/3/library/re.html#re.DOTALL
regex=re.compile(r"\*\*section \d\n---\n(.+?)---\n\n*", re.DOTALL)
matchlist=regex.findall(file)

for m in matchlist:
	print("*** MATCHED ***\n{0}******\n\n".format(m))
