pmr=int(input("enter previous meter reading:"))
cmr=int(input("enter current meter reading:"))
units = pmr-cmr
if units<=400:
	bill=units*4.80
elif units<=500:
	bill=units*6.45
elif units<=600:
	bill=units*8.55
elif units<=800:
	bill=units*9.65
elif units<=1000:
	bill=units*10.70
else:
	bill=units*11.80
print("total bill amounts:",bill)