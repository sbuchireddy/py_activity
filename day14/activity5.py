a=input("enter a:")
b=input("enter b:")
c=input("enter c:")
n={a,b,c}
if len(str(n))>=6 and (a!=b and a!=c and b!=c):
	print("All are unique and non-empty")