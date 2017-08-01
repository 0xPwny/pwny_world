#!/usr/bin/python

#Bugs_Bunny CTF 2107

import libnum

r = open("enc.txt","rb")
f = r.read().split('\n')
flag = ""

for c in f:

	n =20473673450356553867543177537
	p = 2165121523231
	q = 9456131321351327
	e = 17
	phi = (p-1) * (q - 1)
	d = libnum.invmod(e,phi)

	m = pow(int(c),d,n)

	flag += "".join(libnum.n2s(m))
	if "}" in flag:

		print"FLAG : %s\n"% flag