nums = [10,20,30,40,50,60,70,80,90,100] #list
num1 = nums[1::3][::-1]
num2 = nums[0::2]
comb = num1+num2
result = comb*2
print(result)