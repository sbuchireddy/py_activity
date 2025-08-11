a=input("enter a string:")
x=list(a)
x.reverse()
b=''.join(x)
if a==b:
	print("Mirror")
else:
	print("Broken")