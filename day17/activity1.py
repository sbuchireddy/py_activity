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
#eliminating multiples of 3
sieve=[x for x in sieve if x==3 or x%3!=0]
print("iteration 2 after eliminating multiples of 3:",sieve)
#eliminating multiples of 5
sieve=[x for x in sieve if x==5 or x%5!=0]
print("iteration 3 after eliminating multiples of 5:",sieve)
#eliminating multiples of 7
sieve=[x for x in sieve if x==7 or x%7!=0]
print("iteration 4 after eliminating multiples of 7:",sieve)
#now that we eliminated all multiples of 2,3,5,7- we are left with prime numbers
print("final-iteration: the prime numbers between 1-100 are:",sieve)



