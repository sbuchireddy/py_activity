import random
def flip_biased_coin():
	if random.random() < 0.7:
		return "Heads"
	else:
		return "Tails"
print(flip_biased_coin())