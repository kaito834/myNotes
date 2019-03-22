#!/usr/bin/env python
# coding: utf-8
#
# Generate md5 hashsum for HTTP Digest Authentication
# Refer to https://qiita.com/takey/items/1374748d68dda136e137

import getpass
import hashlib

def main():
    username = input("Input Digest Username: ")
    realm = input("Input Digest Realm: ")
    # https://docs.python.org/3/library/getpass.html
    password = getpass.getpass("Input Digest Password: ")

    md5 = hashlib.md5("{0}:{1}:{2}".format(username, realm, password).encode("utf-8")).hexdigest()
    print("{0}:{1}:{2}\n".format(username, realm, md5))

if __name__ == '__main__':
    main()
