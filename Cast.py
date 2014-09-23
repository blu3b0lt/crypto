'''
Copyright (c) 2014 blu3b0lt 

CAST implementation
'''
from Crypto.Cipher import CAST
from Crypto import Random
key = b'Key is 5 to 16'
iv = Random.new().read(CAST.block_size)
cipher = CAST.new(key, CAST.MODE_OPENPGP, iv)
plaintext = raw_input("Enter Text to be Encrypted: ")
msg = cipher.encrypt(plaintext)
print "Encrypted text is: "
print msg
eiv = msg[:CAST.block_size+2]
ciphertext = msg[CAST.block_size+2:]
cipher = CAST.new(key, CAST.MODE_OPENPGP, eiv)
print "Decrypted text is: "
print cipher.decrypt(ciphertext)