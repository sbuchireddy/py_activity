#return gcd
def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1
 
 
print(gcd(48, 18))  
print(gcd(100, 25))
print(gcd(7, 3))