#!/usr/bin/env python
#
# tested by Python 3.4.3 on Windows 8.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

# If you need to access web site/service via proxy, set http_proxy or https_proxy.
# https://docs.python.org/3/library/urllib.request.html#urllib.request.ProxyHandler
# set http_proxy=http://127.0.0.1:8888/
# set https_proxy=https://127.0.0.1:8888/

import urllib.request

# https://docs.python.org/3/library/urllib.request.html#examples
# "Here is an example of doing a PUT request using Request:"
header={'CustomHeader': 'CustomValue'}
req = urllib.request.Request(url='http://127.0.0.1:8080/', headers=header, method='DELETE')
res = urllib.request.urlopen(req, timeout=5)

print(res.status)
print(res.reason)

exit(0)