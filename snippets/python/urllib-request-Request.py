#!/usr/bin/env python
# coding: utf-8
#
# tested by Python 3.4.3 on Windows 8.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

import urllib.request
import ssl

# https://docs.python.org/3/library/urllib.request.html#urllib.request.ProxyHandler
# https://docs.python.org/3.4/howto/urllib2.html#id6
proxyhandler = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:8080/', 'https': 'https://127.0.0.1:8080/'})
# https://www.python.org/dev/peps/pep-0476/
context = ssl._create_unverified_context()
httpshandler =  urllib.request.HTTPSHandler(context=context)
opener = urllib.request.build_opener(proxyhandler, httpshandler)
urllib.request.install_opener(opener)

# By the way, you can use environment variables http_proxy or https_proxy when access web site/service via proxy.
# set http_proxy=http://127.0.0.1:8080/
# set https_proxy=https://127.0.0.1:8080/

# https://docs.python.org/3/library/urllib.request.html#examples
# "Here is an example of doing a PUT request using Request:"
header={'CustomHeader': 'CustomValue'}
req = urllib.request.Request(url='http://127.0.0.1:8888/', headers=header, method='DELETE')
res = urllib.request.urlopen(req, timeout=5)

print(res.status)
print(res.reason)

exit(0)
