#!/usr/bin/env python
#
# I tested by Python 3.4.3 on Windows 8.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

import urllib.request
import getpass

# If you access to url below via Proxy,
# set environment variable 'http_proxy' before execute this.
# And, url scheme is https, then 'https_proxy' must be set instead of 'http_proxy'
url = 'http://192.168.0.1/'

# https://docs.python.org/3/library/functions.html#input
# https://docs.python.org/3/library/getpass.html
auth_user=input('Username: ')
auth_passwd=getpass.getpass('Password: ')

# https://docs.python.org/3.4/howto/urllib2.html#id5
#
# If you would like to Digest Authentication request,
# replace HTTPBasicAuthHandler to HTTPDigestAuthHandler
passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, auth_user, auth_passwd)
authhandler = urllib.request.HTTPBasicAuthHandler(passman)
opener = urllib.request.build_opener(authhandler)
urllib.request.install_opener(opener)

# I can get http.client.HTTPResponse object in variable 'res'
# https://docs.python.org/3/library/http.client.html#httpresponse-objects
#
# ToDo: Error Handling
# https://docs.python.org/3/howto/urllib2.html#handling-exceptions
res = urllib.request.urlopen(url)
res_body = res.read()
print(res_body.decode('utf-8'))
