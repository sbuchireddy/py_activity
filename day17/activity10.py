nums = [4, 2, 4, 3, 2, 2]
freq = {}
 
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
 
result = list(freq.items())
print(result)