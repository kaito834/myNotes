## Self-Signed Certificate
### Environment
- VirtualBox 5.0.16 r105871
- CentOS 6.5
  - CentOS release 6.5 (Final) in /etc/redhat-release
- Apache 2.2.15
  - httpd-2.2.15-47.el6.centos.3.x86_64
  - mod_ssl-2.2.15-47.el6.centos.3.x86_64

### Generating Self-Signed Certificate
At first, you should confirm the version of openssl command.
```
$ openssl version
OpenSSL 1.0.1e-fips 11 Feb 2013
```
A RSA 2048 bits private key is generated in this case. And, this private key
is encrypted by AES-128; option "-aes128" means. You can generate a private
key without encryption. Then, you run openssl command without "-aes128".

You can confirm the details of RSA private key by openssl rsa command with option "-text".
```
$ openssl genrsa -aes128 -out myprivate.key 2048
$ openssl rsa -text -in myprivate.key
```

In next, Certificate Signing Request (CSR) is generated.
According to [OpenSSL Cookbook](https://www.feistyduck.com/library/openssl-cookbook/online/ch-openssl.html#openssl-creating-csrs),
CSR is "*a formal request asking a CA to sign a certificate, and it contains the public key of the entity requesting the certificate and some information about the entity*".
The digest is calculated by SHA-1 in this version of openssl command.
So, the option "-sha256" is set in this case to calculate the digest by SHA-256.

You can confirm the details of CSR by openssl req command with option "-text".
```
$ openssl req -new -sha256 -key myprivate.key -out mycertificate.csr
$ openssl req -text -in mycertificate.csr -noout
```

Finally, the CSR is signed by the private key below. This self-signed certificate
will be expired a year later; this expiration period is based on the option "-days".
The option "-sha256" is set as same as generating CSR.

You can confirm the details of self-signed certificate by openssl x509 commmand with option "-text".
```
$ openssl x509 -req -sha256 -days 365 -in mycertificate.csr -signkey myprivate.key -out mycertificate-selfsigned.crt
$ openssl x509 -text -in mycertificate-selfsigned.crt -noout
```

### Deploy and Enable Self-Signed Certificate on Apache
After changing owner and permission, self-signed certificate and private key
are moved under /etc/pki/tls. This directory is for OpenSSL; you can confirm
this by openssl version command with option "-a". And, the CSR is deleted
because the CSR is not necessary in this case.

It is important that the private key must be limited to access by necessary
applications; the application is Apache in this case. The default private key
contained in mod_ssl package, localhost.key, has similar permission below.
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

At second, you need to modify configuration of Apache.
ssl.conf contains SSL/TLS setting for Apache in this environment.
You need to chanage the paths of SSLCertificateFile and SSLCertificateKeyFile below.
After modifying the ssl.conf, you restart httpd by service command.
```
$ sudo vi /etc/httpd/conf.d/ssl.conf
SSLCertificateFile /etc/pki/tls/certs/mycertificate-selfsigned.crt
SSLCertificateKeyFile /etc/pki/tls/private/myprivate.key
$ sudo service httpd restart
```

Congratulation! Done all steps:)

### References
- [Key and Certificate Management, Chapter 1. OpenSSL, OpenSSL Cookbook](https://www.feistyduck.com/library/openssl-cookbook/online/ch-openssl.html#openssl-key-and-certificate-management)
- [Certificates, SSL/TLS Strong Encryption: FAQ](https://httpd.apache.org/docs/2.4/ssl/ssl_faq.html#aboutcerts)
- [opensslでRSA暗号と遊ぶ](http://d.hatena.ne.jp/ozuma/20130510/1368114329) (in Japanese)
- [オレオレ証明書をopensslで作る（詳細版）](http://d.hatena.ne.jp/ozuma/20130511/1368284304) (in Japanese)


## SSL/TLS Best Practice
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
