'''
Copyright (c) 2014 blu3b0lt 

MD5, SHA256, HMAC implementation
'''
#md5 can not be decrpyted unless you have a dictionary storing all
#all hashes and the original text.
print "MD5:"
from Crypto.Hash import MD5
h = MD5.new()
msg = raw_input("Enter secret text: ")
msg = h.update(msg)
print h.hexdigest()
#sha256 can not be decrpyted unless you have a dictionary storing all
#all hashes and the original text.
print "SHA256:"
from Crypto.Hash import SHA256
h = SHA256.new()
msg = raw_input("Enter secret text: ")
h.update(b'Hello')
print h.hexdigest()

#HMAC
print "HMAC:"
from Crypto.Hash import HMAC
secret = raw_input("Enter passphrase: ")
h = HMAC.new(secret)
msg = raw_input("Enter secret text: ")
h.update(msg)
print h.hexdigest()