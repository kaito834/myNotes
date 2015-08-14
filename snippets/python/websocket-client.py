#!/usr/bin/env python
# coding: utf-8

# websocket-client, https://github.com/liris/websocket-client
# $> C:\Python34\Scripts\pip.exe install websocket-client
# $> C:\Python34\Scripts\pip.exe freeze
# (snip)
# six==1.9.0
# websocket-client==0.32.0
import websocket

def main():
    headers = [
    'X-Custom-Header01: value1',
    'X-Custom-Header02: value2'
    ]

    websocket.enableTrace(True)
    wss = websocket.create_connection("wss://echo.websocket.org/", header=headers)

    print("Sending 'Hello, World'...")
    wss.send('Hello, World')
    print('Sent')
    print('Receving...')
    result = wss.recv()
    print("Received '{0}'".format(result))
    wss.close()

if __name__ == '__main__':
    main()
