#!/usr/bin/env python
# coding: utf-8
#
# Tested by Python 3.5.1 on Windows 8.1
# Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32

import urllib.request
import subprocess

def main():
    url = 'https://github.com/kaito834'
    proxys = {
        'http': 'http://127.0.0.1:8080/',
        'https': 'https://127.0.0.1:8080/'
    }

    #  Initialize urllib.request
    proxyhandler = urllib.request.ProxyHandler(proxys)
    opener = urllib.request.build_opener(proxyhandler)
    urllib.request.install_opener(opener)

    try:
        res = urllib.request.urlopen(url)
        resBody = res.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print('[!] urllib.error.HTTPError: {0}'.format(e))
    except urllib.error.URLError as e:
        # The URLError below raises when urlopen() cannot connect proxy server.
        # <urlopen error [WinError 10061] 対象のコンピューターによって拒否されたため、接続できませんでした。>
        print('[!] urllib.error.URLError: {0}'.format(e))

        print('[!] Launch local proxy because it\'s necessary for this scrpit.')
        print('[!] Plase retry this script!')
        launchLocalProxy()
    except Exception as e:
        print('[!] Exception: {0}'.format(e))

def launchLocalProxy():
    # Burp Suite is executed by subprocess module
    # Ref.
    # https://docs.python.org/3/library/subprocess.html#popen-constructor
    # https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL
    # https://github.com/kaito834/myNotes/blob/master/snippets/python/subprocess_popen.py
    # http://myenigma.hatenablog.com/entry/2016/04/09/184215 (in Japanese)
    cmds = [
        'java',
        '-jar',
        'C:\\Users\\kaito\\Downloads\\burpsuite_free_v1.6.32.jar'
    ]
    subprocess.Popen(cmds, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == '__main__':
    main()
