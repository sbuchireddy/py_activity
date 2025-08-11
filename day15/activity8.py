names=["Alice","Bob","Charlie"]
marks=[85,90,88]
grades=["B","A","A"]
nums=[1,2,3]
for i, names, marks, grades in zip(nums,names, marks, grades):
	print(f"{i},{names},{marks},{grades}")