str = "100020003000400050006000700080009000\x55\x55\x55\x55\xff\xff\xff\x7f"
n = 1000000
for i in range(n-1):
	str += str
print(str)
