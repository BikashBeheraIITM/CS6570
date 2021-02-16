from pwn import *
io = process('./vegas3')
while(1):
	io.sendline("54")
	io.sendline("Bikash")
	x1 = io.recvline().decode(encoding='utf-8')
	x2 = io.recvline().decode(encoding='utf-8')
	x3 = io.recvline().decode(encoding='utf-8')
	x4 = io.recvline().decode(encoding='utf-8')
	x5 = io.recvline().decode(encoding='utf-8')
	print(x1 + x2 + x3 + x4+ x5)
