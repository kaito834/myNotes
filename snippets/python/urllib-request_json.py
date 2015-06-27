#!/usr/bin/env python
#
# tested by Python 3.4.3 on Windows 8.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

import urllib.request
import json

# https://docs.python.org/3/library/urllib.request.html#examples
# https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
# https://docs.python.org/3.4/howto/urllib2.html#id6
proxyhandler = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:8080/', 'https': 'https://127.0.0.1:8080/'})
opener = urllib.request.build_opener(proxyhandler)
urllib.request.install_opener(opener)
res = urllib.request.urlopen('https://ip-ranges.amazonaws.com/ip-ranges.json')
res_body = res.read()

# By the way, you can use environment variables http_proxy or https_proxy when access web site/service via proxy.
# set http_proxy=http://127.0.0.1:8080/
# set https_proxy=https://127.0.0.1:8080/

# https://docs.python.org/3/library/json.html
j = json.loads(res_body.decode("utf-8"))

# parse strings: 'ip_prefix' and 'region'
#for i in range(len(j['prefixes'])):
#	print("{0}\t{1}".format(j['prefixes'][i]['ip_prefix'], j['prefixes'][i]['region']))
for prefix in j['prefixes']:
	print("{0}\t{1}".format(prefix['ip_prefix'], prefix['region']))

exit(0)
