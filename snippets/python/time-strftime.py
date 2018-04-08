#!/usr/bin/env python
# coding: utf-8
# Tested by Python 3.6.1 on Windows 10
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32

# https://docs.python.org/3/library/time.html
# https://docs.python.org/3/library/calendar.html
# 第3章 日付と時刻の処理, Pythonライブラリ厳選レシピ, https://www.amazon.co.jp/dp/B017GT6PC4/
# - datetime, time, python-dateutil, pytz
import time
import calendar

def main():
    # Get current class:time.struct_time instance (UTC/GMT)
    # https://docs.python.org/3/library/time.html#time.gmtime
    # You can get specific class:time_struct_time instance if calls specific epoch seconds as argument
    current_st_utc = time.gmtime()

    # Get current class:time.struct_time instance (Local Timezone)
    # https://docs.python.org/3/library/time.html#time.localtime
    # You can get specific class:time_struct_time instance if calls specific epoch seconds as argument
    current_st_local = time.localtime()

    # https://docs.python.org/3/library/calendar.html#calendar.timegm
    print('Epoch seconds(UTC/GMT): {0}'.format(calendar.timegm(current_st_utc)))
    print('Epoch seconds(Local)  : {0}'.format(calendar.timegm(current_st_local)))

    # https://docs.python.org/3/library/time.html#time.strftime
    # https://stackoverflow.com/questions/19319370/how-do-you-convert-a-python-time-struct-time-object-into-a-iso-string
    print('IS8601 format(UTC/GMT): {0}'.format(time.strftime('%Y-%m-%dT%H:%M:%SZ', current_st_utc)))
    print('IS8601 format(Local  ): {0}'.format(time.strftime('%Y-%m-%dT%H:%M:%SZ', current_st_local)))

if __name__ == '__main__':
    main()
