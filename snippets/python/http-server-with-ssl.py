#!/usr/bin/env python
# coding: utf-8
#
# Tested on Python 3.5.1 on Windows 10

# Based on https://anvileight.com/blog/2016/03/20/simple-http-server-with-python/
# But, use SimpleHTTPRequestHandler instead of BaseHTTPRequestHandler
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

def main(host, port):
    # Set self signed certificate in this snippet.
    # Ref. https://github.com/kaito834/myNotes/blob/master/notes/myNotebookForSSL-TLS.md#generating-self-signed-certificate
    mykeyfile = 'myprivate.key'
    mycertfile = 'mycertificate-selfsigned.crt'

    # https://docs.python.org/3/library/http.server.html#http.server.HTTPServer
    # https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler
    httpd = HTTPServer((host, port), SimpleHTTPRequestHandler)
    # https://docs.python.org/3/library/ssl.html#ssl.wrap_socket
    httpd.socket = ssl.wrap_socket (httpd.socket, keyfile=mykeyfile, certfile=mycertfile, server_side=True)
    print("Start HTTPS server: https://{0}:{1}".format(host, str(port))).
    print("CAUTION: Files under current directory will be accessed via https://{0}:{1}/.".format(host, str(port)))
    httpd.serve_forever()

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 3:
        main(argv[1], int(argv[2]))
    else:
        print("Usage: {0} <ip address/host name> <port>".format(argv[0]))
        exit(1)
