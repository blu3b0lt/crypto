'''
Copyright (c) 2014 blu3b0lt 

DES3 implementation
'''
from Crypto.Cipher import DES3
from Crypto import Random
key = b'DES is very old!'
iv = Random.new().read(DES3.block_size)
cipher = DES3.new(key, DES3.MODE_OFB, iv)
print "Enter text to be encrypted: "
plaintext = raw_input()
msg = iv + cipher.encrypt(plaintext)
print "Encrypted msg is: "
print msg
cipher = DES3.new(key, DES3.MODE_OFB, iv)
msg = cipher.decrypt(msg[DES3.block_size:]).decode('utf-8')
print "Decrypted text is: "
print msg