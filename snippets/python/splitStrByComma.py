#!/usr/bin/env python
# tested by Python 3.4.3 on Windows 8.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

def main():
    numbers = []

    str = input('Please input numbers separated by comma: \n> ')

    # https://docs.python.org/3/library/stdtypes.html#string-methods
    # p.87, 4.2.5 リストのメソッド, ”Python文法詳解", O'REILLY
    #
    # You can use CSV library if you read values from CSV file.
    # https://docs.python.org/3/library/csv.html
    # pp.156-160 8.1 CSVファイルを扱う, 'Pythonライブラリ厳選レシピ', http://gihyo.jp/book/2015/978-4-7741-7707-6
    for n in str.split(','):
        n = n.strip()
        if(n.isdecimal() and 0 <= int(n) <= 10 and numbers.count(int(n)) == 0):
            numbers.append(int(n))

    for n in numbers:
        print(n)

if __name__ == '__main__':
    main()
