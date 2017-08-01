#revbasic1


x = "2926232f".decode("hex")[::-1] + "2f333125".decode("hex")[::-1] + "2315222b".decode("hex")[::-1] 
x += "3d15393e".decode("hex")[::-1]
x += "0f15392b".decode("hex")[::-1] + "3f2e1510".decode("hex")[::-1]+"372f2e".decode("hex")[::-1]

v = "J"*len(x)

z = zip(x,v)

flag = ""

for d,o in z:
	do = chr(ord(d)^ord(o))
	flag += "".join(do)

print "[+FLAG+] : " + flag
#print len(flag)