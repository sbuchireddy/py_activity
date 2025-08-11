'''
square = lambda x:x**2
>>> print(square(5))
'''
'''
my_list=(1,2,3,4,5,6)
result=list(map(lambda x:x**3 if (x%2!=0) else x**2,my_list))
print(result)
'''
'''
my_list=(1,2,3,4,5)
result=list(map(lambda x:x**2,my_list))
print(result)
[1, 4, 9, 16, 25]
my_list=(1,2,3,4,5,6,7,8,9,101)
result=list(filter(lambda x:x%2==0,my_list))
print(result)
[2, 4, 6, 8]
my_list=(1,2,3,4,5,6,7,8,9,10)
result=list(filter(lambda x:x%2==0,my_list))
print(result)
'''
'''
from functools import reduce
my_list=[1,2,3,4,5]
result=reduce(lambda x,y:x*y, my_list)
print(result)
'''
'''
squares=[x*x for x in range(5)]
print(squares)
'''
'''
even_squares = []
for num in range(11):
    if num % 2 == 0:
        even_squares.append(num ** 2)

print(even_squares)
'''
'''
even_squares = [num ** 2 for num in range(11) if num % 2 == 0]
print(even_squares)
'''
'''
prime_numbers = []
for num in range(2, 50):  # checking numbers from 2 to 49
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

print(prime_numbers)
'''
'''
labels=[f'{x}:even' if x%2==0 else f'{x}:odd' for x in range(5)]
print(labels)
'''
'''
pairs=[(y,x) for x in range(2) for y in range(3)]
print(pairs)
'''
'''
squares={x:x**2 for x in range(3)}
print(squares)
'''
'''
squares = {x: x**2 for x in range(10) if x % 2 != 0}
print(squares)
'''
'''
my_list = ['one', 'two', 'three', 'four', 'five']
for index, value in enumerate(my_list, start=1):
    print(f"{index}:{value}")

'''
'''
squares=(x*x for x in range(5))
print(squares)
print(next(squares))
print(list(squares))
'''
'''
try:
	v1=int(input("enter the integer values:"))
except valueerror:
	v1=int(input("correct numeric value:"))
	print(v1)
'''
data = {'a': 1, 'b': 2, 'c': 1}

swapped = {}

for key in data:
    value = data[key]
    if value in swapped:
        swapped[value].append(key)
    else:
        swapped[value] = [key]

# Convert lists to tuples
for value in swapped:
    swapped[value] = tuple(swapped[value])

print(swapped)
