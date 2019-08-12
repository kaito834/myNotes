## My Usage of *openssl* Command
Environment:
- Windows 10
- OpenSSL 1.0.2h  3 May 2016; included [Git for Windows 2.9.0](https://git-scm.com/download/win)

### Parse SSL/TLS Certificate
Retrieve SSL/TLS certificate by [openssl s_client](https://www.openssl.org/docs/manmaster/apps/s_client.html) with "-showcerts" option. You need '-proxy' option too if you access via proxy server; Note old *openssl* command [is not implemented the '-proxy' option](http://stackoverflow.com/questions/3220419/openssl-s-client-using-a-proxy).

For the example below, SSL/TLS certificate on www.openssl.org is retrieved. The SSL/TLS certificate is base64 encoded strings between '-----BEGIN CERTIFICATE-----' and '-----END CERTIFICATE-----'. *openssl s_client* command will output all certificates if certificates are chained. Save the certificate you want to parse into text file.
```
$ openssl s_client -connect www.openssl.org:443 -showcerts
CONNECTED(000001B0)
---
Certificate chain
 0 s:/OU=Domain Control Validated/CN=*.openssl.org
   i:/C=BE/O=GlobalSign nv-sa/CN=GlobalSign Domain Validation CA - SHA256 - G2
-----BEGIN CERTIFICATE-----
MIIE9TCCA92gAwIBAgISESHQqr5sLPE1xTXWmA7ABqljMA0GCSqGSIb3DQEBCwUA
MGAxCzAJBgNVBAYTAkJFMRkwFwYDVQQKExBHbG9iYWxTaWduIG52LXNhMTYwNAYD
VQQDEy1HbG9iYWxTaWduIERvbWFpbiBWYWxpZGF0aW9uIENBIC0gU0hBMjU2IC0g
RzIwHhcNMTQxMDA5MjAyOTAwWhcNMTcxMTEyMTcxNDA1WjA7MSEwHwYDVQQLExhE
b21haW4gQ29udHJvbCBWYWxpZGF0ZWQxFjAUBgNVBAMMDSoub3BlbnNzbC5vcmcw
ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCkfg71ZYW6VtWDbDEmAfDw
CAKVJ260FAP6gANjS8eO+0drZe6MexIA5htR/sYhG8PIsJnKBuxiQ9KwMbRwLxBU
HcuBACT3MNif1DsFWuNCMFsTDPrfJzLOgoPo+4lQ0QYARwMJhxelA0P9rcTwBACY
6QRZgfAJ5iezz69GJkmrDGZIUoAR+PFF7xR/rzFaBMH7gbok0UJRKFPxO5fyiSfc
ZvSmMV/AZcUGVmxE9HLBQ6QCTbAdGAdVlHHxFPVb9Of9Ze/KJg8VIwFl5Hw+RQCj
+OjtBPkSwNQ9r0Bwc2c7uRnRpojERHxlo7Tn8uJ+LYcCkWcaVc8+JbjF78F8E417
AgMBAAGjggHMMIIByDAOBgNVHQ8BAf8EBAMCBaAwSQYDVR0gBEIwQDA+BgZngQwB
AgEwNDAyBggrBgEFBQcCARYmaHR0cHM6Ly93d3cuZ2xvYmFsc2lnbi5jb20vcmVw
b3NpdG9yeS8wJQYDVR0RBB4wHIINKi5vcGVuc3NsLm9yZ4ILb3BlbnNzbC5vcmcw
CQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwQwYDVR0f
BDwwOjA4oDagNIYyaHR0cDovL2NybC5nbG9iYWxzaWduLmNvbS9ncy9nc2RvbWFp
bnZhbHNoYTJnMi5jcmwwgZQGCCsGAQUFBwEBBIGHMIGEMEcGCCsGAQUFBzAChjto
dHRwOi8vc2VjdXJlLmdsb2JhbHNpZ24uY29tL2NhY2VydC9nc2RvbWFpbnZhbHNo
YTJnMnIxLmNydDA5BggrBgEFBQcwAYYtaHR0cDovL29jc3AyLmdsb2JhbHNpZ24u
Y29tL2dzZG9tYWludmFsc2hhMmcyMB0GA1UdDgQWBBQPVUooul4mMU0KrqGTBtQ6
ZtRofjAfBgNVHSMEGDAWgBTqTnzUgC3lFYGGJoyCbcCYpM+XDzANBgkqhkiG9w0B
AQsFAAOCAQEAiJDoinZmR2M9Zlap1DM9WOHgwIMot154eNPZyf27rYxv9kekdTAp
9fesfBScMzq9NCyzy8rtWxMCPyhpCXh9iibkC3Yon+sj/gZSrNNh2nfeKhuroBxi
alaGRjg1WHNKx4Wc5dGm+chJCZFWOk1NzB8JZQQcSNt3IFyDWSScEGXwiVe1VbUa
tYIohSiWzvFMEfj7YoXt6tihYqEJG42jBg7MhaUtI4rUSDC5LB20Zhv0OG5CRORj
Wg8Iz2SUXkH8F1RJo+kMbCC/DFeII/ZTrF+B7qRVvLkctlLcukylqvsE1vibozQb
0A8/RZkfkqobqnkLnYeLUSCWNx/AHm8L5w==
-----END CERTIFICATE-----
 1 s:/C=BE/O=GlobalSign nv-sa/CN=GlobalSign Domain Validation CA - SHA256 - G2
   i:/C=BE/O=GlobalSign nv-sa/OU=Root CA/CN=GlobalSign Root CA
(snip)
```

Parse the text file by *openssl x509* command with '-in' and '-text' options.
```
$ openssl.exe x509 -in a.pem -text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            11:21:d0:aa:be:6c:2c:f1:35:c5:35:d6:98:0e:c0:06:a9:63
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=BE, O=GlobalSign nv-sa, CN=GlobalSign Domain Validation CA - SHA256 - G2
        Validity
            Not Before: Oct  9 20:29:00 2014 GMT
            Not After : Nov 12 17:14:05 2017 GMT
        Subject: OU=Domain Control Validated, CN=*.openssl.org
(snip)
```

## Self-Signed Certificate
### Environment
- VirtualBox 5.0.16 r105871
- CentOS 6.5
  - CentOS release 6.5 (Final) in /etc/redhat-release
- Apache 2.2.15
  - httpd-2.2.15-47.el6.centos.3.x86_64
  - mod_ssl-2.2.15-47.el6.centos.3.x86_64

### Generating Self-Signed Certificate
First, confirm the version of openssl command.
```
$ openssl version
OpenSSL 1.0.1e-fips 11 Feb 2013
```
A RSA 2048 bits private key is generated in this case. And, this private key
is encrypted by AES-128; option "-aes128". To generate a private
key without encryption, run openssl command without "-aes128".

To confirm the details of RSA private key, run openssl rsa command with option "-text".
```
$ openssl genrsa -aes128 -out myprivate.key 2048
$ openssl rsa -text -in myprivate.key
```

Next, Certificate Signing Request (CSR) is generated.
According to [OpenSSL Cookbook](https://www.feistyduck.com/library/openssl-cookbook/online/ch-openssl.html#openssl-creating-csrs),
CSR is "*a formal request asking a CA to sign a certificate, and it contains the public key of the entity requesting the certificate and some information about the entity*".
The digest is calculated by SHA-1 in this version of openssl command.
So, the option "-sha256" is set in this case to calculate the digest by SHA-256.

Need to set option '--config' with the path for openssl.cnf if openssl.cnf is not found; Related post on stackoverflow is [here](http://stackoverflow.com/questions/7360602/openssl-and-error-in-reading-openssl-conf-file). Error:'Unable to load config info from /usr/local/ssl/openssl.cnf' has raised by openssl command included in [Git for Windows](https://git-scm.com/download/win).

To confirm the details of CSR, run openssl req command with option "-text".
```
$ openssl req -new -sha256 -key myprivate.key -out mycertificate.csr
$ openssl req -text -in mycertificate.csr -noout
```

Finally, the CSR is signed by the private key as below. This self-signed certificate
will expire a year later; this expiration period is based on the option "-days".
To set an option "-sha256" is the same as generating CSR.

To confirm the details of the self-signed certificate, run openssl x509 command with option "-text".
```
$ openssl x509 -req -sha256 -days 365 -in mycertificate.csr -signkey myprivate.key -out mycertificate-selfsigned.crt
$ openssl x509 -text -in mycertificate-selfsigned.crt -noout
```

If necessary, openssl x509 command with "-fingerprint" confirms
the SHA-1 fingerprint of the self-signed certificate. Moreover, to confirm
the SHA-256 fingerprint, run with "-sha256".
```
$ openssl x509 -fingerprint -in mycertificate-selfsigned.crt -noout
$ openssl x509 -fingerprint -sha256 -in mycertificate-selfsigned.crt -noout
```

### Deploy and Enable Self-Signed Certificate on Apache
After changing owner and permission, self-signed certificate and private key
are moved to /etc/pki/tls. This directory is for OpenSSL; to confirm
this, run openssl version command with option "-a". And, the CSR is deleted
because the CSR is not necessary in this case.

It is important that necessary applications can only access the private key;
the application is Apache in this case. The default private key
contained in mod_ssl package, localhost.key, has similar permission as below.
```
$ rm mycertificate.csr
$ sudo chown apache:apache mycertificate-selfsigned.crt myprivate.key
$ sudo chmod 400 myprivate.key
$ sudo mv mycertificate-selfsigned.crt /etc/pki/tls/certs/
$ sudo mv myprivate.key /etc/pki/tls/private/
```
```
$ ls -l /etc/pki/tls/private/
total 8
4 -rw------- 1 root   root   1675 Mar 12 06:00 localhost.key
4 -r-------- 1 apache apache 1766 Mar 12 10:41 myprivate.key
```

Second, modify the configuration of Apache.
ssl.conf contains SSL/TLS setting for Apache in this environment.
Change the paths of SSLCertificateFile and SSLCertificateKeyFile as below.
After modifying the ssl.conf, restart httpd by service command.
```
$ sudo vi /etc/httpd/conf.d/ssl.conf
SSLCertificateFile /etc/pki/tls/certs/mycertificate-selfsigned.crt
SSLCertificateKeyFile /etc/pki/tls/private/myprivate.key
$ sudo service httpd restart
```

Congratulations! Done all steps:)

### References
- [Key and Certificate Management, Chapter 1. OpenSSL, OpenSSL Cookbook](https://www.feistyduck.com/library/openssl-cookbook/online/ch-openssl.html#openssl-key-and-certificate-management)
- [Certificates, SSL/TLS Strong Encryption: FAQ](https://httpd.apache.org/docs/2.4/ssl/ssl_faq.html#aboutcerts)
- [opensslでRSA暗号と遊ぶ](http://d.hatena.ne.jp/ozuma/20130510/1368114329) (in Japanese)
- [オレオレ証明書をopensslで作る（詳細版）](http://d.hatena.ne.jp/ozuma/20130511/1368284304) (in Japanese)

## SSL/TLS Best Practice
- [プロフェッショナル SSL/TLS](https://www.lambdanote.com/products/tls) (in Japanese)
  - Japanese Translation of "Bulletproof SSL and TLS", Ivan Ristić
- [Transport Layer Protection Cheat Sheet, OWASP](https://www.owasp.org/index.php/Transport_Layer_Protection_Cheat_Sheet)
- [SSL/TLS Deployment Best Practices(PDF), Qualys SSL Labs](https://www.ssllabs.com/downloads/SSL_TLS_Deployment_Best_Practices.pdf)
  - via https://www.ssllabs.com/projects/best-practices/index.html
  - 1.2. Protect Private Keys, 1. Private Key and Certificate
    - Restrict access to private Key
    - Generate private key and CSR on trusted computer
    - Protect private key by password in backup system
      - *Private key passwords don’t help much in production because a knowledgeable attacker can always retrieve the keys from process memory*
    - Revoke old certificate and generate new key after compromise
    - Renew certificate every year, always with new private key
- [Security/Server Side TLS, Mozilla Wiki](https://wiki.mozilla.org/Security/Server_Side_TLS)
