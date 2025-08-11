n = int(input("Enter a number: "))
 
if n < 2:
    print("Not prime")
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
 
    if is_prime:
        print("Prime")
    else:
        print("Not prime")
 