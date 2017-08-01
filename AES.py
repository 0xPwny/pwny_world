#! /usr/bin/env python

from Crypto.Cipher import AES
from Crypto import Random
import string
import itertools




comb = "OoWwAaSsPp" #Guessed 

f = open("enc","rb").read()

calc =itertools.combinations_with_replacement(comb, 5)


iv = '0'*10+"\x00"*6 #IV WEAKNESS

for paswd in calc:

	key = "".join(paswd)*4+"2017" 
	cipher = AES.new(key, AES.MODE_CBC, iv )
	dec = cipher.decrypt(f)
	
	if "OWASP" in dec:
		print "KEY : %s"% "".join(paswd)
		print "FLAG: %s"% dec