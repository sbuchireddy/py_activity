sum_of_odds=0
for num in range(1,100):
	if num%2!=1:
		sum_of_odds=num+sum_of_odds
print("the sum of the odd numbers between 1 to 100 are",sum_of_odds)