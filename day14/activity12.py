nums=list(map(int,input("enter numbers:").split(',')))
if nums==sorted(nums):
	print("ascending")
elif nums==(sorted(nums)[::-1]):
	print("descending")
else:
	print("unordered")