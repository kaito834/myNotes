#!/usr/bin/env python
# coding: utf-8
#
# I tested by Python 3.4.3 on Windows 10.
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

import urllib.request
import urllib.error
import xml.etree.ElementTree

'''NOTICE
According to Python document, xml.etree.ElementTree module is not secure
against malicious XML attack. The document recommends to use defusedxml or
defusedexpat package.

References:
- https://docs.python.org/3/library/xml.html
- https://docs.python.org/3/library/xml.html#xml-vulnerabilities
- https://docs.python.org/3/library/xml.html#defused-packages
'''
def main():
    # Parse XML file which has some namespaces
    # This spnippet parse response of MyJVN API, http://jvndb.jvn.jp/apis/.
    myJvnApi_url = 'http://jvndb.jvn.jp/myjvn?method=getProductList&maxCountItem=3&lang=en&keyword=sdk'

    try:
        res = urllib.request.urlopen(myJvnApi_url)
        resBody = res.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print('[!] urllib.error.HTTPError: {0}'.format(e))
    except urllib.error.URLError as e:
        print('[!] urllib.error.URLError: {0}'.format(e))
    except Exception as e:
        print('[!] Exception: {0}'.format(e))

    print('## MyJVN API XML file:')
    print(resBody)
    xmlElement = xml.etree.ElementTree.fromstring(resBody)

    # https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml-with-namespaces
    # https://docs.python.org/3/library/xml.etree.elementtree.html#xpath-support
    # http://stackoverflow.com/questions/14853243/parsing-xml-with-namespace-in-python-via-elementtree
    namespace = {'mjres': 'http://jvndb.jvn.jp/myjvn/Results'}
    print('## for child in xmlElement.findall(\'.//mjres:Vendor\', namespace):')
    for child in xmlElement.findall('.//mjres:Vendor', namespace):
        print("Attribute:{0}\tText:{1}".format(child.attrib, child.text))
    print('')

if __name__ == '__main__':
    main()
