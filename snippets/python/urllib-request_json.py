#!/usr/bin/env python
# coding: utf-8
#
# tested by Python 3.4.3 on Windows 8.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

import urllib.request
import json
import ssl

# https://docs.python.org/3/library/urllib.request.html#examples
# https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
# https://docs.python.org/3.4/howto/urllib2.html#id6
proxyhandler = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:8080/', 'https': 'https://127.0.0.1:8080/'})
opener = urllib.request.build_opener(proxyhandler)
urllib.request.install_opener(opener)
# https://www.python.org/dev/peps/pep-0476/
# This script disables certificate verfication, but this is *NOT* recommended.
# If you use self-signed certificate, you should add your root certificate by SSLContext.load_cert_chain()
# https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain
# https://docs.python.org/3/library/ssl.html#ssl-security
context = ssl._create_unverified_context()
res = urllib.request.urlopen('https://ip-ranges.amazonaws.com/ip-ranges.json', context=context)
# type(res_body) is class 'bytes'
res_body = res.read()

# By the way, you can use environment variables http_proxy or https_proxy when access web site/service via proxy.
# set http_proxy=http://127.0.0.1:8080/
# set https_proxy=https://127.0.0.1:8080/

# https://docs.python.org/3/library/json.html#json.loads
# *Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object using this conversion table.*
# type(j) is class 'dict'
j = json.loads(res_body.decode("utf-8"))

# Output Escaped ASCII CR+LF if json.dumps() is outputed directly; print(json.dumps())
# type(j_str) is class 'str'
# Ref.
# https://docs.python.org/3/library/json.html#json.dumps
# *Serialize obj to a JSON formatted str using this conversion table.*
# http://stackoverflow.com/questions/16318543/cant-pretty-print-json-from-python
# http://stackoverflow.com/questions/9785049/python-how-to-use-json-dumps-on-windows
j_str = json.dumps(j, ensure_ascii=True, sort_keys=True, indent=4)
print(j_str)
print('='*3)

# parse strings: 'ip_prefix' and 'region'
#for i in range(len(j['prefixes'])):
#	print("{0}\t{1}".format(j['prefixes'][i]['ip_prefix'], j['prefixes'][i]['region']))
for prefix in j['prefixes']:
	print("{0}\t{1}".format(prefix['ip_prefix'], prefix['region']))

exit(0)
