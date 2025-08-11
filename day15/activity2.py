s=input("type a sentance:").lower()
vowels="aeiou"
count=0
for vow in s:
	if vow in vowels:
		count=count+1
print("the number of vowels are:",count)
