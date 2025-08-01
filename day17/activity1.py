'''
n=int(input("enter a number:"))
for num in range(2,n+1):
	count=0
	for i in range(1,num+1):
		if num % i== 0:
			count=count+1
	if count==2:
		print(num,',',end=' ')
'''
n=int(input("enter a number:"))
sieve=list(range(2,n+1))
print("initial list:",sieve)
#eliminating multiples of 2
sieve=[x for x in sieve if x==2 or x%2 !=0]
print("iteration 1 after eliminating multiples of 2:",sieve)

