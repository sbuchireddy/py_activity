n=int(input("enter a number:"))
for num in range(1,n+1):
	space=' '*(n-1)
	print(space*'*'*2*num-1)
	