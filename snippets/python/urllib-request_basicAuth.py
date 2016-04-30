#!/usr/bin/env python
#
# I tested by Python 3.4.3 on Windows 8.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

import urllib.request
import urllib.error
import getpass
import os

# If you access to url below via Proxy,
# you can use environment variable 'http_proxy' without urllib.request.ProxyHandler.
# And, url scheme is https, then 'https_proxy' must be set instead of 'http_proxy'
url = 'http://192.168.0.1/'
# https://docs.python.org/3.4/howto/urllib2.html#id6
proxyhandler = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:8080/', 'https': 'https://127.0.0.1:8080/'})

# https://docs.python.org/3/library/functions.html#input
# https://docs.python.org/3/library/getpass.html
auth_user=input('Username: ')
# https://docs.python.org/3/library/os.html#os.getenv
# Please set X_GW_BASIC_PASSWORD as environment variable before executing this snippet
if os.getenv('X_GW_BASIC_PASSWORD') is None:
    auth_passwd=getpass.getpass('Password: ')
else:
    print('Set Password from environment variable, X_GW_BASIC_PASSWORD.')
    auth_passwd=os.getenv('X_GW_BASIC_PASSWORD')

# https://docs.python.org/3.4/howto/urllib2.html#id5
#
# If you would like to Digest Authentication request,
# replace HTTPBasicAuthHandler to HTTPDigestAuthHandler
passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, auth_user, auth_passwd)
authhandler = urllib.request.HTTPBasicAuthHandler(passman)
opener = urllib.request.build_opener(authhandler, proxyhandler)
urllib.request.install_opener(opener)

# I can get http.client.HTTPResponse object in variable 'res'
# https://docs.python.org/3/library/http.client.html#httpresponse-objects
try:
    res = urllib.request.urlopen(url)
    res_body = res.read()
    print(res_body.decode('utf-8'))
except urllib.error.HTTPError as e:
    # https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError
    print('[!] urllib.error.HTTPError: {0}'.format(e))
    if e.code == 401:
        print('[!] User name or password on Basic Authentication is not correct.')
except urllib.error.URLError as e:
    # https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError
    # Confirmed that this was raised when I could not connect proxy server
    print('[!] urllib.error.URLError: {0}'.format(e))
except Exception as e:
    print('[!] Exception: {0}'.format(e))
