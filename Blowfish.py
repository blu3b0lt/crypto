'''
Copyright (c) 2014 blu3b0lt 

Blowfish implementation
'''
from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack
bs = Blowfish.block_size
key = b'Long key len from 4 to 56 bytes'
iv = Random.new().read(bs)
cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
plaintext = raw_input("Enter secret message: ")
plen = bs - divmod(len(plaintext),bs)[1]
padding = [plen]*plen
padding = pack('b'*plen, *padding)
msg = iv + cipher.encrypt(plaintext + padding)
print "Encrypt message: "
print msg
cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
msg = cipher.decrypt(msg[Blowfish.block_size:]).decode('utf-8')
print "Decrypted text is: "
print msg

'''
Input should be a multiple of 8, if not it is padded automatically, 
so that the result will contain extra characters.
'''