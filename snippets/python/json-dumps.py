#!/usr/bin/env python
# coding: utf-8
# I tested by Python 3.4.3 on Windows 8.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

def main():
    import json, traceback

    '''
    Sample Dictionary is below;
    {
    'id': 123,
    'objects': [
        {'str2': 'fuga', 'str1': 'hoge'},
        {'str2': 'fuga', 'str1': 'hoge'}
        ]
    }
    '''
    jsonDic = {}
    jsonDic['id'] = 123
    # List Comprehensions, https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    jsonDic['objects'] = [{"str1":"hoge", "str2":"fuga"} for i in range(2)]

    print('## This converts following dictionary to JSON object')
    print(jsonDic)

    # https://docs.python.org/3/library/json.html#json.dumps
    # *Serialize obj to a JSON formatted str using this conversion table.*
    print("## json.dumps(jsonDic, ensure_ascii=True, sort_keys=True)")
    print(json.dumps(jsonDic, ensure_ascii=True, sort_keys=True))
    print("## json.dumps(jsonDic, ensure_ascii=True, sort_keys=True, indent=4)")
    print(json.dumps(jsonDic, ensure_ascii=True, sort_keys=True, indent=4))

    # Add key 12345(int) and value 'test'(string) to jsonDic
    # TypeError raised with Python 3.4.3 or 3.5.1 on Windows 8.1; detail is "unorderable types: int() < str()"
    # No TypeError raise if 12345 is replaced to '12345', class str
    #
    # Accroding to Notes in https://docs.python.org/3/library/json.html#json.dumps,
    # it is corret even though the key of dictionary is class int
    jsonDic[12345] = 'test'
    try:
        print("## Added key 12345(int) and value 'test'(string) to jsonDic")
        print("## json.dumps(jsonDic, ensure_ascii=True, sort_keys=True, indent=4)")
        print(json.dumps(jsonDic, ensure_ascii=True, sort_keys=True, indent=4))
    except TypeError as e:
        # p.181 5.5 例外処理, ”Python文法詳解", O'REILLY
        # https://docs.python.org/3/library/traceback.html#traceback.print_exc
        print('[!] TypeError raised: {0}'.format(e))
        traceback.print_exc()

if __name__ == '__main__':
    main()
