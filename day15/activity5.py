'''
n=int(input("enter a integer:"))
count=0
while n>=0:
	n=n-3
	count=count+1
	print("ran for",count,"times")
'''

n=int(input("enter a integer:"))
count=0
for i in range(n,-3):
	count+=1
	print("ran for",count,"times")

