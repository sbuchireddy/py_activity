def check_even(x):
    if x % 2 == 0:
        return x
    else:
        raise ValueError("Number is odd")
 
try:
    num = int(input("Enter a number: "))
    print("Even number:", check_even(num))
except ValueError as e:
    print("Error:", e)