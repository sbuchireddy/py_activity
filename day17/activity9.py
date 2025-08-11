n = int(input("Enter a number: "))
 
num_str = str(n)
power = len(num_str)
total = 0
 
for digit in num_str:
    total += int(digit) ** power
 
if total == n:
    print("True")   # It's an Armstrong number
else:
    print("False")  # Not an Armstrong number