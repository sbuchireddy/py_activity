def f(x, lst=list):
	lst=lst()
	lst.append(x)
	return lst
print(f(1))
print(f(2))