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
```
$ curl http://127.0.0.1/
```
Then, the HTTP request was below:
```
GET / HTTP/1.1
User-Agent: curl/7.41.0
Host: 127.0.0.1
Accept: */*

```
The curl with no options outputs only body of HTTP response.
An option [-i/--include](http://curl.haxx.se/docs/manpage.html#-i) allows you output all of HTTP response.
Or, an option [-I/--head](http://curl.haxx.se/docs/manpage.html#-I) allows you output only headers of HTTP response.
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
For example, SSL certificate problem raises when you access to HTTPS site via Burp Suite.
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

An option [-k/--insecure](http://curl.haxx.se/docs/manpage.html#-k) allows you accept invalid SSL certificate.
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
#### Reference
- [-d/--data, curl.1 the man page](http://curl.haxx.se/docs/manpage.html#-d)
