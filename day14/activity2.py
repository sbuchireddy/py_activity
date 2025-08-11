username=input("enter username:")
password=input("enter password:")
if username=="admin" and (password=="secret123" or password=="letmein"):
	print("access granted")
else:
	print("access denied")