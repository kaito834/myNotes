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
    # This snippet parses sample XML on https://docs.python.org/3/library/xml.etree.elementtree.html#parsing-xml.
    # I saved the XML file as "sample.xml" and run http.server.
    #   $> python.exe -m http.server --bind 127.0.0.1 8080
    sampleXml_url = 'http://127.0.0.1:8080/sample.xml'

    try:
        res = urllib.request.urlopen(sampleXml_url)
        resBody = res.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print('[!] urllib.error.HTTPError: {0}'.format(e))
    except urllib.error.URLError as e:
        print('[!] urllib.error.URLError: {0}'.format(e))
    except Exception as e:
        print('[!] Exception: {0}'.format(e))

    print('## Sample XML file:')
    print(resBody)

    # https://docs.python.org/3/library/xml.html
    # https://docs.python.org/3/library/xml.etree.elementtree.html
    xmlElement = xml.etree.ElementTree.fromstring(resBody)
    print('## xml.etree.ElementTree.fromstring(resBody)')
    print(type(xmlElement))
    print('')

    print('## for child in xmlElement:')
    for child in xmlElement:
        print("Attribute:{0}\tText:{1}".format(child.attrib, child.text))
    print('')

    # https://docs.python.org/3/library/xml.etree.elementtree.html#finding-interesting-elements
    print('## for child in xmlElement.iter(\'year\'):')
    for child in xmlElement.iter('year'):
        print("Attribute:{0}\tText:{1}".format(child.attrib, child.text))
    print('')

if __name__ == '__main__':
    main()
