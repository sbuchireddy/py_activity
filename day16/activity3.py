import random
secret=random.randint(1,100)
attempts=0
while True:
	guess=int(input("enter your guessed input between (1-100):"))
	attempts=attempts+1

	if guess<secret:
		print("Too Low")
	if guess>secret:
		print("Too High")
	if guess==secret:
		print("correct")
		break

