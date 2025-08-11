a=int(input("enter first integer:"))
b=int(input("enter second integer:"))
if a %b == 0 or b %a == 0:
	print(max(a,b))
else:
	print(a+b)