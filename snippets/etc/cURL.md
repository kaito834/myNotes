## Environment
- curl 7.41.0 on Windows
  - It was installed with msysgit 1.9.5

```
$ curl --version
curl 7.41.0 (i386-pc-win32) libcurl/7.41.0 OpenSSL/0.9.8zf zlib/1.2.8
Protocols: dict file ftp ftps gopher http https imap imaps ldap ldaps pop3 pop3s rtsp smtp smtps telnet tftp
Features: AsynchDNS IPv6 Largefile SSPI Kerberos SPNEGO NTLM SSL libz
```

## My usage of cURL
### Basic
The curl with no options outputs only body of HTTP response.
```
$ curl http://127.0.0.1/
<html><body><h1>hi!</h1></body></html>
```
Then, the HTTP request was below:
```
GET / HTTP/1.1
User-Agent: curl/7.41.0
Host: 127.0.0.1
Accept: */*

```

Progress meter is outputted if the output of curl is piped. You can use [-s/--slient](https://curl.haxx.se/docs/manpage.html#-s) option if you would like not to output progress meter.
```
$ curl -S https://ip-ranges.amazonaws.com/ip-ranges.json | jq-win64.exe .createDate
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  113k  100  113k    0     0   125k      0 --:--:-- --:--:-- --:--:--  127k
"2017-04-07-18-22-10"

$ curl -s https://ip-ranges.amazonaws.com/ip-ranges.json | jq-win64.exe .createDate
"2017-04-07-18-22-10"
```

#### Reference
-  [https://orebibou.com/2016/03/curl%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%81%A7%E8%A6%9A%E3%81%88%E3%81%A6%E3%81%8A%E3%81%8D%E3%81%9F%E3%81%84%E4%BD%BF%E3%81%84%E6%96%B9xx%E5%80%8B/#5]

### Output HTTP response and request
An option [-i/--include](http://curl.haxx.se/docs/manpage.html#-i) allows you to output all of HTTP response; Both headers and body of HTTP response.
Or, an option [-I/--head](http://curl.haxx.se/docs/manpage.html#-I) allows you to output **only** headers of HTTP response.
```
$ curl -i http://127.0.0.1/
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.4.3
Date: Thu, 03 Sep 2015 14:13:23 GMT
Content-type: text/html

<html><body><h1>hi!</h1></body></html>
$ curl -I http://127.0.0.1/
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.4.3
Date: Thu, 03 Sep 2015 14:14:06 GMT
Content-type: text/html

```
If you would like to output HTTP request on STDIN, you should execute curl with --trace-ascii or -v options.
An option [--trace-ascii](http://curl.haxx.se/docs/manpage.html#--trace-ascii) with '-' allows you to output HTTP request; both headers and body of HTTP request. The output for curl w/ --trace-ascii contains debug strings, so it is better to filter those strings.
Or an option [-v](http://curl.haxx.se/docs/manpage.html#-v) allows you to output **only** headers of HTTP request.
```
$ curl --trace-ascii - -X POST -d a=aaa http://127.0.0.1/
== Info:   Trying 127.0.0.1...
== Info: Connected to 127.0.0.1 (127.0.0.1) port 80 (#0)
=> Send header, 142 bytes (0x8e)
0000: POST / HTTP/1.1
0011: User-Agent: curl/7.41.0
002a: Host: 127.0.0.1
003b: Accept: */*
0048: Content-Length: 5
005b: Content-Type: application/x-www-form-urlencoded
008c:
=> Send data, 5 bytes (0x5)
0000: a=aaa
== Info: upload completely sent off: 5 out of 5 bytes
== Info: HTTP 1.0, assume close after body
<= Recv header, 17 bytes (0x11)
0000: HTTP/1.0 200 OK
<= Recv header, 35 bytes (0x23)
0000: Server: BaseHTTP/0.6 Python/3.4.3
<= Recv header, 37 bytes (0x25)
0000: Date: Tue, 27 Oct 2015 12:41:08 GMT
<= Recv header, 25 bytes (0x19)
0000: Content-type: text/html
<= Recv header, 2 bytes (0x2)
0000:
<= Recv data, 40 bytes (0x28)
0000: <html><body><h1>POST!</h1></body></html>
<html><body><h1>POST!</h1></body></html>== Info: Closing connection 0

$ curl --trace-ascii a.txt -X POST -d a=aaa http://127.0.0.1/
<html><body><h1>POST!</h1></body></html>
$ grep -E "^[0-9a-f]{4}\:" a.txt | cut -c 7-
POST / HTTP/1.1
User-Agent: curl/7.41.0
Host: 127.0.0.1
Accept: */*
Content-Length: 5
Content-Type: application/x-www-form-urlencoded

a=aaa
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.4.3
Date: Tue, 27 Oct 2015 13:14:02 GMT
Content-type: text/html

<html><body><h1>POST!</h1></body></html>

$ curl -v -X POST -d a=aaa http://127.0.0.1/
*   Trying 127.0.0.1...
* Connected to 127.0.0.1 (127.0.0.1) port 80 (#0)
> POST / HTTP/1.1
> User-Agent: curl/7.41.0
> Host: 127.0.0.1
> Accept: */*
> Content-Length: 5
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 5 out of 5 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Server: BaseHTTP/0.6 Python/3.4.3
< Date: Tue, 27 Oct 2015 12:44:14 GMT
< Content-type: text/html
<
<html><body><h1>POST!</h1></body></html>* Closing connection 0
```

### Range 'Globbing'
```
$ curl http://127.0.0.1/user00[1-3]/{one,two}
```
Then, six HTTP request were sent; Please see below
```
127.0.0.1 - - [03/Sep/2015 22:14:14] "GET /user001/one HTTP/1.1" 200 -
127.0.0.1 - - [03/Sep/2015 22:14:14] "GET /user002/one HTTP/1.1" 200 -
127.0.0.1 - - [03/Sep/2015 22:14:14] "GET /user003/one HTTP/1.1" 200 -
127.0.0.1 - - [03/Sep/2015 22:14:14] "GET /user001/two HTTP/1.1" 200 -
127.0.0.1 - - [03/Sep/2015 22:14:14] "GET /user002/two HTTP/1.1" 200 -
127.0.0.1 - - [03/Sep/2015 22:14:14] "GET /user003/two HTTP/1.1" 200 -
```
#### Reference
- [URL, curl.1 the man page](http://curl.haxx.se/docs/manpage.html#URL)

### Send HTTP Request via HTTP Proxy
```
$ curl --proxy http://127.0.0.1:8080/ http://127.0.0.1/
```
#### Reference
- [-x/--proxy, curl.1 the man page](http://curl.haxx.se/docs/manpage.html#-x)

### Accept invalid SSL certificate
For example, SSL certificate problem raises when you access HTTPS site via Burp Suite.
Then, self signed certificate by Portswigger.net was not installed on Windows.
```
$ curl --proxy https://127.0.0.1:8080/ https://www.ipa.go.jp/
curl: (60) SSL certificate problem: self signed certificate in certificate chain

More details here: http://curl.haxx.se/docs/sslcerts.html

curl performs SSL certificate verification by default, using a "bundle"
 of Certificate Authority (CA) public keys (CA certs). If the default
 bundle file isn't adequate, you can specify an alternate file
 using the --cacert option.
If this HTTPS server uses a certificate signed by a CA represented in
 the bundle, the certificate verification probably failed due to a
 problem with the certificate (it might be expired, or the name might
 not match the domain name in the URL).
If you'd like to turn off curl's verification of the certificate, use
 the -k (or --insecure) option.
```

An option [-k/--insecure](http://curl.haxx.se/docs/manpage.html#-k) allows you to accept invalid SSL certificate.
```
$ curl -k --proxy https://127.0.0.1:8080/ https://www.ipa.go.jp/
```

### Send POST Request
```
$ curl -X POST -d a=aaa -d b=bbb http://127.0.0.1/
```
Then, the HTTP request was below.
```
POST / HTTP/1.1
User-Agent: curl/7.41.0
Host: 127.0.0.1
Accept: */*
Content-Length: 11
Content-Type: application/x-www-form-urlencoded

a=aaa&b=bbb
```
A option [-d/--data](http://curl.haxx.se/docs/manpage.html#-d) allows you to read body from file or STDIN.
A sample is below. In this example, HTTP body was read from 'sample.xml'.
Then, value of Content-Type is same as the HTTP request above; application/x-www-form-urlencoded.
```
$ curl -i -X POST -d @sample.xml http://127.0.0.1/
```
You can change the value of Content-Type by a option [-H](http://curl.haxx.se/docs/manpage.html#-H).
```
$ curl -i -X POST -d @sample.xml -H 'Content-Type: application/xml' http://127.0.0.1/
```

#### Reference
- [-d/--data, curl.1 the man page](http://curl.haxx.se/docs/manpage.html#-d)
- [Appendix A, Red Hat Enterprise Virtualization 3.0 REST API Guide](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Virtualization/3.0/html/REST_API_Guide/appe-REST_API_Guide-cURL_Integration.html)

### Send HTTP Request w/ Authorization Header
#### Basic Authentication
```
$ curl --basic -u user http://192.168.0.1/
Enter host password for user 'user': *****
```

#### Digest Authentication
```
$ curl --digest -u user http://192.168.0.1/
```

#### References
- [--basic, curl.1 the man page](http://curl.haxx.se/docs/manpage.html#--basic)
- [--digest, curl.1 the man page](http://curl.haxx.se/docs/manpage.html#--digest)

### Send HTTP request with multipart body
You can use '-H' and '-F' options if you would like to send HTTP request with multipart bodies. The sample curl command with them and the HTTP request are as follows:
```
$ curl -X POST -H "Content-Type: multipart/mixed" -F name="@sample.json;type=application/json" -F "name=@sample.jpg;type=image/jpeg" http://127.0.0.1/
```
```
POST / HTTP/1.1
User-Agent: curl/7.41.0
Host: 127.0.0.1
Accept: */*
Content-Length: 509
Expect: 100-continue
Content-Type: multipart/mixed; boundary=------------------------7240fd359b06b012


--------------------------7240fd359b06b012
Content-Disposition: form-data; name="name"; filename="sample.json"
Content-Type: application/json

{
  "id": 123,
  "objects": [
    {
      "str1": "hoge",
      "str2": "fuga"
    },
    {
      "str1": "fuga",
      "str2": "hoge",
    }
  ]
}

--------------------------7240fd359b06b012
Content-Disposition: form-data; name="name"; filename="sample.jpg"
Content-Type: image/jpeg

sample jpeg
--------------------------7240fd359b06b012--
```

'-F' option allows you to send HTTP request with over one multipart bodies. According to cURL manual, this HTTP request is based on [RFC2388](https://www.ietf.org/rfc/rfc2388.txt). '@sample.json' on '-H' option above indicates to read contents from file, sample.json. ';type=application/json' is optional; semi-column is just a separator. You can include Content-Type header in multipart body if you would like to set it.

You execute curl command with only -F option, and the value of Content-type header is 'multipart/form-data'. If the value is not good for you, you should execute with '-H' option that have 'Content-Type: XXX' as the value. For example, '-H' option with 'Content-Type: multipart/mixed' allows you to change value of Content-Type header from 'multipart/form-data' to 'multipart/mixed'.

#### Reference
- [-H, --header, curl.1 the man page](http://curl.haxx.se/docs/manpage.html#-H)
- [-F, --form, curl.1 the man page](http://curl.haxx.se/docs/manpage.html#-F)
- [Curl: Re: Multipart/mixed from Config File](http://curl.haxx.se/mail/archive-2010-03/0049.html)
- [send a HTTP request which Content-Type is 'multipart/mixed' by cURL, GitHub Gist](https://gist.github.com/kaito834/12244be613c6e6b1c59a)
