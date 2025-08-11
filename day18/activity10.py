input_str = "Banana"
vowels = "aeiou"

found_vowels = set(char for char in input_str.lower() if char in vowels)

for vowel in sorted(found_vowels):
	print(vowel)