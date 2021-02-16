str = "100020003000400050006000700080009000\x55\x55\x55\x55\xff\xff\xff\x7f\x0a"
i = 1
while(i < 1000000):
	str += str
	i += i
print(str)
