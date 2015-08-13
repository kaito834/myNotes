#!/usr/bin/env python
# coding: utf-8
# I tested this on Windows 10/Python 3.4.3 w/Pycrpto 2.6.1
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32

# https://github.com/dlitz/pycrypto/blob/master/Doc/pycrypt.rst
# Get Windows binary from http://www.voidspace.org.uk/python/pycrypto-2.6.1/
from Crypto.Cipher import AES
from Crypto import Random

def main():
    # List members of Crypto.Chiper.AES
    # https://docs.python.org/3/howto/sorting.html
    print('### vars(AES)')
    for key in sorted(vars(AES)):
        if key == 'block_size':
            print(' ', '{0}: {1}'.format(key, AES.block_size))
        elif key == 'key_size':
            print(' ', '{0}: {1}'.format(key, AES.key_size))
        else:
            print(' ', key)

    # Encrypt and decrypt by AES-128, CBC mode
    print('### AES.new(key, AES.MODE_CBC, iv)')

    # Input plaintext
    # http://stackoverflow.com/questions/20852664/python-pycrypto-encrypt-decrypt-text-files-with-aes
    ptext = input('Please input plaintext: ')
    ptext_bytes = ptext.encode('utf-8')
    if len(ptext) % AES.block_size != 0:
        print('[!] Plaintext is NOT multiple of {0} bytes, so plaintext will be padded by 0.'.format(AES.block_size))
        ptext_bytes +=  b'\0' * ( AES.block_size - len(ptext_bytes) % AES.block_size )
        print('[!] Padded plaintext: {0} (length is {1})'.format(ptext_bytes, len(ptext_bytes)))

    # Generate encryption key and IV(Initial Vector)
    key = Random.new().read(AES.block_size)
    iv  = Random.new().read(AES.block_size)
    print("\nGenerated key and IV(Initial Vector) by Crypo.Random.new().read():")
    print(' key: {0} (length is {1})'.format(key, len(key)))
    print(' IV : {0} (length is {1})'.format(iv, len(iv)))

    # Encrypt plain text by AES-128, CBC mode; perhaps w/ padding
    aes128cbc = AES.new(key, AES.MODE_CBC, iv)
    ebytes = aes128cbc.encrypt(ptext_bytes)
    print("\nEncrypted plaintext by AES-128, CBC mode:")
    print(' Encrypted text: {0} (length is {1})'.format(ebytes, len(ebytes)))

    # Decrypt ecrypted text to plain text
    aes128cbc = AES.new(key, AES.MODE_CBC, iv)
    dtext_bytes = aes128cbc.decrypt(ebytes).rstrip(b"\0")
    dtext = dtext_bytes.decode('utf-8')
    print("\nDecrypted ecrypted text to plain text:")
    print(' Plain text: {0} (length is {1})'.format(dtext, len(dtext_bytes)))

    '''NOTES:
    If AES.new(key) is called, mode is set 1 by default.
    That means that ECB mode is specified.
    >>> from Crypto.Cipher import AES
    >>> aes = AES.new('1234567890123456')
    >>> vars(aes)
    {'block_size': 16, 'IV': b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '_cipher': <_AES object at 0x0254C6F0>, 'mode': 1}

    AESCipher object encrypts plain text, and the same object decrypts the encrypted text.
    Then, decryption will fail.
    >>> from Crypto.Cipher import AES
    >>> aes = AES.new(b'1234567890123456', AES.MODE_CBC, b'1234567890123456')
    >>> enc = aes.encrypt('1234567890123456')
    >>> plain = aes.decrypt(enc)
    >>> enc
    b'\xd8\xb5\x98H\xc7g\x0c\x94\xb2\x9bT\xd27\x9e.z'
    >>> plain
    b'\xd8\xb5\x98H\xc7g\x0c\x94\xb2\x9bT\xd27\x9e.z'
    >>> aes = AES.new(b'1234567890123456', AES.MODE_CBC, b'1234567890123456')
    >>> aes.decrypt(enc)
    b'1234567890123456'
    '''

if __name__ == '__main__':
    main()
