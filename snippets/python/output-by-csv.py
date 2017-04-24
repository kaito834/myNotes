#!/usr/bin/env python
# coding: utf-8
# Tested by Python 3.6.1 on Windows 10
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32

import csv

def main():
    output = ["test", "hoge,hoge", "\"fuga\",\"fuga\""]

    # https://docs.python.org/3/library/functions.html#open
    # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    # https://docs.python.org/3/reference/compound_stmts.html#the-with-statement
    # Output:
    # test,hoge,hoge,"fuga","fuga"
    with open("output-not-used-csv.csv", "w", encoding="utf-8") as f:
        f.write(",".join(output))

    # https://docs.python.org/3/library/csv.html#csv.writer
    # Output:
    # test,"hoge,hoge","""fuga"",""fuga"""
    with open("output-used-csv.csv", "w", newline='', encoding="utf-8") as f:
        csvwriter = csv.writer(f)
        # https://docs.python.org/3/library/csv.html#csv.csvwriter.writerow
        csvwriter.writerow(output)

if __name__ == '__main__':
    main()
