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
import time
import threading

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


    We can get response headers as dict type from headers member of WebSocket instance.
    >>> import websocket
    >>> wss = websocket.create_connection("wss://echo.websocket.org/")
    >>> wss.headers
    {'date': 'sat, 15 aug 2015 04:04:19 gmt', 'server': 'kaazing gateway', 'upgrade': 'websocket', 'connection': 'upgrade', 'sec-websocket-accept': 'l3ltqc+2pngmvwelrpudewb2nua='}
    '''

    print("[!] Sending 'Hello, World'...")
    wss.send('Hello, World')
    print('[!] Sent')
    print('[!] Receving...')
    result = wss.recv()
    print("[!] Received '{0}'".format(result))

    print("[!] Send ping frame on every 5 seconds...")
    # https://github.com/kaito834/myNotes/blob/master/snippets/python/threading_infiniteLoop.py
    thread_event = threading.Event()
    thread = threading.Thread(target=sendPingFrame, args=(wss, thread_event, 5))
    thread.start()

    print('[!] Start infinite loop to send \'Hello, World!\' every 8 seconds.')
    print('[!] NOTE: The loop will finish if you will press [Ctrl+C].')
    while True:
        try:
            wss.send('Hello, World!')
            print('[!] Sent \'Hello, World!\'.')
            data = wss.recv()
            print("[!] Received '{0}'".format(data))
            time.sleep(8)
        except KeyboardInterrupt:
            thread_event.set()
            break

    wss.close()

# https://github.com/kaito834/myNotes/blob/master/snippets/python/threading_infiniteLoop.py
def sendPingFrame(wsObj, stop_event, sleep_time):
    while(not stop_event.is_set()):
        wsObj.ping()
        print('[!] Sent PING frame.')
        stop_event.wait(sleep_time)

if __name__ == '__main__':
    main()
