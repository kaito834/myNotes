#!/usr/bin/env python
# coding: utf-8

# websocket-client, https://github.com/liris/websocket-client
# $> C:\Python34\Scripts\pip.exe install websocket-client
# $> C:\Python34\Scripts\pip.exe freeze
# (snip)
# six==1.9.0
# websocket-client==0.32.0
import websocket
import ssl

def main():
    headers = [
    'X-Custom-Header01: value1',
    'X-Custom-Header02: value2'
    ]

    websocket.enableTrace(True)
    wss = websocket.create_connection("wss://echo.websocket.org/", header=headers)
    '''
    Arguments: http_proxy_host and http_pory_port are necessary
    if websocket connection via proxy will be established;
    I tested Burp Suite Free Edition 1.6.01, https://portswigger.net/burp/downloadfree.html.

    References:
    - https://github.com/liris/websocket-client#http-proxy
    - https://github.com/liris/websocket-client#how-to-disable-ssl-cert-verification

    wss = websocket.create_connection("wss://echo.websocket.org/", header=headers,
        http_proxy_host='127.0.0.1', http_proxy_port=8080,
        sslopt={"cert_reqs": ssl.CERT_NONE})
    '''

    print("Sending 'Hello, World'...")
    wss.send('Hello, World')
    print('Sent')
    print('Receving...')
    result = wss.recv()
    print("Received '{0}'".format(result))
    wss.close()

if __name__ == '__main__':
    main()
