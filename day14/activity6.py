a,b=map(int, input("enter a,b:").split(' '))
a=a^b
b=a^b
a=a^b
print(a,b)

